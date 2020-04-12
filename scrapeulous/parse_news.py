import csv
from datetime import datetime
import sys

BANNED_DOMAIN_LIST = [
    # CNN
    'http://lite.cnn.com',
    'https://lite.cnn.com',
    'https://cnnespanol.cnn.com',
    'http://www.cnn.com/TRANSCRIPTS', # 新聞稿
    'https://e.newsletters.cnn.com', # 轉址
    # BBC
    'https://www.bbc.com/news/localnews',
    'https://www.bbc.com/mundo',
    'https://www.bbc.com/somali',
    'https://www.bbc.com/gahuza',
    'https://www.bbc.com/pidgin',
    'https://www.bbc.com/programmes',
    'https://www.bbc.com/swahili',
    'https://www.bbc.com/portuguese',
    'https://www.bbc.com/tamil',
    'https://www.bbc.com/learningenglish',
    'http://www.bbc.com/learningenglish',
    'https://www.bbc.com/igbo',
    'https://www.bbc.com/hausa',
    'https://www.bbc.com/urdu',
    'https://www.bbc.com/afrique',
    'https://www.bbc.com/yoruba',
    'https://www.bbc.com/japanese',
    'https://www.bbc.com/sounds',
    'https://www.bbc.com/sport',
    'https://www.bbc.com/punjabi',
]

UK_BBC_URL_WHITELIST = [
    'https://www.bbc.com/news/uk'
]

KEYWORD_LIST = [
    'coronavirus',
    'Coronavirus',
    'pneumonia',
    'Wuhan',
    'covid19'
    'Covid19',
    'COVID19',
    'covid-19',
    'Covid-19'
    'COVID-19',
    'nCOVID',
    'nCOVID19',
    'nCOVID-19',
]

OUTRAGE_COMPONENTS = [
    ' death',
    ' deaths',
    'at risk for coronavirus',
    'at risk for c',
    'kill',
    'kills',
    'lockdown',
    'the potential impact',
    'possibly',
    'possible',
    'could',
    'could threaten',
    'threaten',
    ' cases',
    ' more',
    'anonymous',
    'catastrophe',
    'catastrophic',
    'tragedy',
    'tragic',
    ' die',
    'dead ',
    ' severe',
    'expected to kill',
    'expected',
    ' terror',
    'disagree',
    'conflict',
    'be patient',
    'calm down',
    'don\'nt worry',
    'no need to worry',
    'not to worry',
    'deadly',
    'fatal',
    'lethal',
    'dread',
    'violence',
    'in a mad rush', # 瘋搶
    'panic buying',
    'frantic',
    'panic',
    'lunatic',
    'crazy',
    'hoarding',
    'death toll',
    'Death toll',
    'toll hits',
    'wary eye',
    'accelerated its spread',
    'silent spread',
    'outbreak',
    'fatality rate',
    'grave situation',
    'not added to official',
    'unofficial',
    'died',
    'leak',
    'cases will be MUCH higher',
    'MUCH',
    'mysterious',
]

def sort_news(filename, show_no_date_urls=False):
    date_count = {}
    err_count = 0
    line_count = 0
    corona_news_count = 0
    outrage_news_count = 0
    delimiter = '!&^'

    f = open(filename, 'r')
    line = f.readline()
    while line:
        line_count += 1
        if 'Article `download()` failed' in line or 'You must `parse()` an article first!' in line:
            err_count += 1
            line = f.readline()
            continue

        tokens = line.split(delimiter)

        if 'bbc' in filename or 'cnn' in filename:
            # URL_FILTER
            url = tokens[4]
            if 'bbc' in filename:
                keep_this_news = False
                for w_url in UK_BBC_URL_WHITELIST:
                    if w_url in url and '/comments' not in url:
                        keep_this_news = True
                        break
                if not keep_this_news:
                    err_count += 1
                    line = f.readline()
                    continue
            else:
                skip_this_news = False
                for banned_domain in BANNED_DOMAIN_LIST:
                    if banned_domain in url:
                        skip_this_news = True
                        break
                if skip_this_news:
                    err_count += 1
                    line = f.readline()
                    continue

            # date check
            date = tokens[0]
            if date and date != 'None' and '2020' in date:
                date = tokens[0][:10] # %Y-%m-%d
            else:
                if show_no_date_urls:
                    print(f'{url}')
                err_count += 1
                line = f.readline()
                continue

            short_title = tokens[1]
            parsed_title = tokens[2]
            keywords = eval(tokens[3])

            # coronavirus news check
            for keyword in keywords:
                if keyword in KEYWORD_LIST:
                    corona_news_count += 1
                    for component in OUTRAGE_COMPONENTS:
                        # 純看 title
                        if component in short_title or component in parsed_title:
                            outrage_news_count += 1
                            val = date_count.get(date, 0)
                            date_count[date] = val + 1
                            break
                    break
        else:
            # URL_FILTER
            url = tokens[5]
            #print(url)
            skip_this_news = False
            for banned_domain in BANNED_DOMAIN_LIST:
                if banned_domain in url:
                    skip_this_news = True
                    break
            if skip_this_news:
                err_count += 1
                line = f.readline()
                continue

            # date check
            date = tokens[1][:10]
            if date and date != 'None' and '2020' in date:
                pass
            else:
                if show_no_date_urls:
                    print(f'{url} got no date')
                err_count += 1
                line = f.readline()
                continue

            short_title = tokens[2]
            parsed_title = tokens[3]
            keywords = eval(tokens[4])

            # coronavirus news check
            for keyword in KEYWORD_LIST:
                if keyword in keywords or keyword in short_title or keyword in parsed_title:
                    corona_news_count += 1
                    # print(parsed_title)
                    for component in OUTRAGE_COMPONENTS:
                        # 純看 title
                        if component in short_title or component in parsed_title:
                            print(component)
                            # print(short_title, parsed_title, component)
                            outrage_news_count += 1
                            val = date_count.get(date, 0)
                            date_count[date] = val + 1
                            break
                    break

        line = f.readline()
        continue

    # count news by week
    sorted_date_count = {}
    sorted_week_count = {}
    for date in sorted(date_count):
        dt = datetime.strptime(date, '%Y-%m-%d')
        sorted_date_count[date] = date_count[date]

        week = dt.isocalendar()[1]
        val = sorted_week_count.get(week, 0)
        sorted_week_count[week] = val + date_count[date]

    print(f'{line_count} news read')
    print(f'{err_count} news got kicked out')
    print(f'{corona_news_count} news are related to coronavirus')
    print(f'{outrage_news_count} news may lead to outrage')
    print(sorted_date_count)
    print(sorted_week_count)
    f.close()
    return


def check_error_news(filename):
    f = open(filename, 'r')
    delimiter = '!&^'
    wf = open(filename + 'error_news.txt', 'w')

    total_news = 0
    error_news = 0
    line = f.readline()
    while line:
        total_news += 1
        if 'Article `download()` failed' in line or 'You must `parse()` an article first!' in line:
            error_news += 1
            tokens = line.split(delimiter)
            if 'bbc' in filename or 'cnn' in filename:
                date = tokens[0][-12:]
                url = tokens[-2]
                wf.write(f'{date}{delimiter}{url}\n')
            else:
                date = tokens[1]
                url = tokens[-1]
                wf.write(f'{date}{delimiter}{url}')

            line = f.readline()
            continue
        line = f.readline()
    f.close()
    wf.close()
    print(f'{error_news} news lost out of {total_news}, lost rate {error_news / total_news}')


cmd = sys.argv[1]
filename = sys.argv[2]

if __name__ == '__main__':
    if cmd == 'sort':
        sort_news(filename)
    elif cmd == 'check':
        check_error_news(filename)
    else:
        print('invalid cmd')
