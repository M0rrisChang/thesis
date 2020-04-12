from datetime import datetime, timedelta
import json
import sys
import warnings

import requests
from newspaper import Article

API_KEY_LIST = [
    'xwrfuPbZBp2DPeGtEh2GUP-Fn82NTfV1PSHie_lovRA', # r07
    'tL6aZ_TQutITQ7C7VGwATWDL9aFM64HRyckMbWknr50',
    'LpQNW3PAVQigEaGSjHCZj9T-7TJ7XZAidlD7V_2cpoE',
]


def scrape(start_date, API_KEY_LIST):
    url = 'https://scrapeulous.com/api'
    items = [f'site://www.nytimes.com/{start_date.replace("-", "/")}/us coronavirus']

    # make sure sufficient credits
    for API_KEY in API_KEY_LIST:
        payload = {
            "API_KEY": API_KEY,
            "function": "https://raw.githubusercontent.com/NikolaiT/scrapeulous/master/google_scraper.js",
            "items": items,
            "can_use_proxies": True,
            "region": "us",
            "options": {
                "google_params": {
                    "num": 50,
                },
                "num_pages": 50,
            }
        }

        r = requests.post(url, data=json.dumps(payload), verify=False)
        results = r.json()
        error = ''
        if isinstance(results, dict):
            error = results.get('error')

        if error == 'remaining credits not sufficient for this api call':
            print(f'{API_KEY} got no credits. Switching API_KEY')
        elif error == 'Invalid api key':
            print(f'{API_KEY} is invalid. Switching API_KEY')
        else:
            break

    # extract links from SERP
    news_list = []
    urls = []
    for res in results:
        if isinstance(res['result'], list):
            for page in res['result']:
                for link in page['results']:
                    news = {}
                    url = link['link']
                    if url in urls:
                        continue
                    else:
                        urls.append(url)
                    news['url'] = url
                    news['date'] = link['date']
                    news['title'] = link['title']
                    news_list.append(news)
            print(start_date, len(news_list), 'news scraped')
        elif isinstance(res['result'], dict):
            print(start_date, len(news_list), 'news scraped.', res['result']['error_message'])
        elif isinstance(res['result'], str):
            print(results)

    filename = start_date + '.csv'
    f = open(filename, 'w')
    f.write(str(news_list))
    f.close()

    return len(news_list)


def process_news(news_list):
    filter_domains = [
    ]

    filtered = []
    for news in news_list:
        badboy = False
        for f in filter_domains:
            if f in news['url']:
                badboy = True
                break
        if not badboy:
            filtered.append(news)

    f = open('nytimes_us.txt', 'a')
    for news in filtered:
        error, parsed_title, keywords = '', '', ''
        date = news['date']

        try:
            url = news['url']
            article = Article(url)
            # 這裡本來SSL憑證有時會出錯，把套件中network.py的get_html_2XX_only中的verify=False補上即可繞掉
            article.download()
            article.parse()
            article.nlp()
            keywords = article.keywords
            parsed_title = article.title

            if not date:
                date = article.publish_date
            else:
                date = datetime.strptime(date, '%b %d, %Y')
        except Exception as e:
            error = str(e)

        delimiter = '!&^'
        line = f'{error}{delimiter}{date}{delimiter}{news["title"]}{delimiter}{parsed_title}{delimiter}{keywords}{delimiter}{url}\n'
        print(line[:-1])
        f.write(line)
    f.close()

    # TODO: 研究寫檔資料格式（讀黨要方便）、error logging、filtered_domains、BBC


def cmd_scrape(date):
    while True:
        dt = datetime.strptime(date, '%Y-%m-%d')

        scrape(date, API_KEY_LIST)

        next_dt = dt + timedelta(days=1)
        if next_dt > datetime(2020, 4, 3):
            break
        date = next_dt.strftime('%Y-%m-%d')


def cmd_process(date):
    # process day by day
    while True:
        dt = datetime.strptime(date, '%Y-%m-%d')
        end_date = (dt + timedelta(days=1)).strftime('%Y-%m-%d')
        filename = date + '.csv'
        f = open(filename, 'r')
        news_list = eval(f.readline())
        print(f'processing {len(news_list)} news on {date}')

        process_news(news_list)

        next_dt = dt + timedelta(days=1)
        if next_dt > datetime(2020, 3, 30):
            break
        date = next_dt.strftime('%Y-%m-%d')


def cmd_check(date):
    # process day by day
    is_all_clear = True
    while True:
        dt = datetime.strptime(date, '%Y-%m-%d')
        filename = date + '.csv'
        f = open(filename, 'r')
        news_list = eval(f.readline())
        if news_list == []:
            print(f'0 news on {date}. Restart scraping ...')
            news_num = scrape(date, API_KEY_LIST)
            if news_num == 0:
                is_all_clear = False
        else:
            print(f'{len(news_list)} news on {date}.')

        next_dt = dt + timedelta(days=1)
        if next_dt > datetime(2020, 4, 3):
            break
        date = next_dt.strftime('%Y-%m-%d')

    return is_all_clear


cmd = sys.argv[1]
start_date = sys.argv[2]

if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    if cmd == 'scrape':
        # scrape news
        cmd_scrape(start_date)
    elif cmd == 'check':
        # check wheter intactly scraped or not
        is_all_clear = cmd_check(start_date)
        while not is_all_clear:
            is_all_clear = cmd_check(start_date)
    elif cmd == 'process':
        # process scraped_news into csv (keywords appended)
        cmd_process(start_date)
    else:
        print('invalid cmd')
