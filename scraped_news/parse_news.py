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

CORONA_KEYWORD_LIST = [
    'coronavirus',
    'Coronavirus',
    'Coronovirus',
    'pneumonia',
    'Wuhan',
    'covid19'
    'Covid19',
    'COVID19',
    'covid-19',
    'Covid-19',
    'COVID-19',
    'nCOVID',
    'nCOVID19',
    'nCOVID-19',
    'China virus',
    'China Virus',
    'china virus',
    'Chinese Virus',
    'Chinese virus',
    'chinese virus',
    '冠狀病毒',
    '新冠',
    '新冠肺炎',
    '新型冠狀病毒',
    '新型冠狀肺炎',
    '武漢肺炎',
    '疫情',
    '確診',
    '',
]

CORONA_KEYWORD_LIST += [
    '新型コロナウイルス',
    '新型コロナ',
]

MANDARIN_OUTRAGE_COMPONENTS = [
    '再增', '激增', '暴增', '又增', '狂增', '猛增',
    '又傳', '再添', '延燒', '延燒',
	'搶購', '囤貨', '匿名', '推測', '預測', '分歧',
    '對立', '不必', '疏失', '誤判', '死亡', '身亡',
    '致命', '隱匿', '隱瞞', '疑染',
    '例！', '恐慌', '死！', '慘死', '肆虐', '陳屍',
    '不治', '煉獄', '致死', '驚！', '疫情擴大', '重創',
    '群聚感染', '傳封城', '將封城', '恐封城', '不排除封城',
    '看不見終點', '沒有終點', '淪為', '慘絕人寰',
    '警惕', '恫！', '恐怖！', '引爆', '再新增', '曝光',
    '機密', '恐留', '淪陷', '衝擊', '狂燒',
    '死亡風險高', '蔓延', '疑似', '爆發', '恐成', '恐將',
    '疑社區感染', '院內感染', '恐損', '專家：', '慘況', '不明',
    '可能死亡', '嚴重',
    #'新冠', '肺炎',
]

JAPANESE_OUTRAGE_COMPONENTS = [
    '大量発生',
]

OUTRAGE_COMPONENTS = [
    ' death', 'Death',
    'at risk for coronavirus',
    'at risk for c',
    'kill', 'Kill',
    'lockdown', 'Lockdown',
    'the potential impact',
    'possibl', 'Possibl',
    'could', 'Could',
    'threaten', 'Threaten',
    ' more', 'More',
    'anonymous',
    'catastroph', 'Catastroph',
    'tragedy', 'Tragedy',
    'tragic', 'Tragic',
    ' die', 'Die',
    'dead ', 'Dead',
    ' severe', 'Severe',
    'expected to kill',
    'expected', 'Expected',
    ' terror', 'Terror',
    'disagree',
    'conflict',
    'be patient',
    'calm down', 'Calm Down',
    'don\'t worry', 'Don\'t Worry',
    'no need to worry',
    'not to worry',
    'deadly', 'Deadly',
    'fatal', 'Fatal',
    'dread', 'Dread',
    'violence', 'Violence'
    'in a mad rush', # 瘋搶
    'panic buying', 'Panic Buying',
    'frantic', 'Frantic',
    'panic', 'Panic',
    'lunatic', 'Lunatic',
    'crazy', 'Crazy',
    'hoard', 'Hoard',
    'death toll',
    'Death toll',
    'toll hits', 'Toll',
    'wary eye',
    'spread', 'Spread',
    'outbreak', 'Outbreak',
    'fatality rate',
    'grave situation',
    'not added to official',
    'unofficial',
    'leak', 'Leak'
    'cases will be MUCH higher',
    'MUCH',
    'mysterious',
    'will have infect', 'Will Have Infect',
    'may have', 'May Have',
    'fear', 'Fear',
    'shaken', 'Shaken',
    'crisis', 'Crisis',
    'suggests', 'Suggests',
    'suspected coronavirus patient', 'Suspected Coronavirus Patient',
    'suspected patient',
    'coronavirus enters', 'Coronavirus Enters',
    'coronavirus hits', 'Coronavirus Hits',
    'Hit by Coronavirus', 'hit by corona',
    'Struck by Coronavirus', 'struck by corona',
    'stay home', 'Stay Home',
    'nightmare', 'Nightmare',
    'havoc', 'Havoc',
    'disrupt', 'Distrupt',
] + MANDARIN_OUTRAGE_COMPONENTS + JAPANESE_OUTRAGE_COMPONENTS


def sort_news(filename, from_date, to_date, show_no_date_urls=False):
    component_count = {}
    for c in OUTRAGE_COMPONENTS:
        component_count[c] = 0
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

        # URL_FILTER
        try:
            url = tokens[5]
        except Exception:
            print(tokens)
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
            if (datetime.strptime(date, '%Y-%m-%d') < datetime.strptime(from_date, '%Y-%m-%d') or
                    datetime.strptime(date, '%Y-%m-%d') > datetime.strptime(to_date, '%Y-%m-%d')):
                line_count -= 1
                line = f.readline()
                continue
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
        outrageous = False
        related = False
        for keyword in CORONA_KEYWORD_LIST:
            if keyword in keywords or keyword in short_title or keyword in parsed_title:
                corona_news_count += 1
                related = True
                #print(parsed_title)
                for component in OUTRAGE_COMPONENTS:
                    # 純看 title
                    if component in short_title or component in parsed_title:
                        #print(component)
                        #print(f'!!!{component}!!!{parsed_title or short_title}')
                        component_count[component] += 1
                        outrage_news_count += 1
                        val = date_count.get(date, 0)
                        date_count[date] = val + 1
                        outrageous = True
                        break
                break

        if not related:
            #print(parsed_title)
            pass
        if related and not outrageous:
            #print(parsed_title)
            pass

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
    start_date = ''
    end_date = ''
    l = []
    for k in sorted_date_count:
        if not start_date:
            start_date = k
        l.append(sorted_date_count[k])
        end_date = k

    acc_l = []
    for i in range(len(l)):
        if i > 0:
            acc_l.append(l[i] + acc_l[i - 1])
        else:
            acc_l = [l[i]]
    print(f'from {start_date} to {end_date}')
    print(l)
    print(acc_l)
    #print(component_count)
    #print(sorted_week_count)
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
country = sys.argv[2]
from_date = sys.argv[3]
to_date = sys.argv[4]

if __name__ == '__main__':
    filename = f'all_{country}_news.txt'
    if cmd == 'sort':
        sort_news(filename, from_date, to_date)
    elif cmd == 'check':
        check_error_news(filename)
    else:
        print('invalid cmd')

    print(OUTRAGE_COMPONENTS)