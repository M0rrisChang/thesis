import sys

us_filenames = [
    'us_cnn_news/us_cnn_news.txt',
    'us_foxnews/us_foxnews.txt',
    'us_huffpost/us_huffpost.txt',
    'us_nytimes/us_nytimes.txt',
]

uk_filenames = [
    'uk_bbc_news/uk_bbc_news.txt',
    'uk_the_guardian/uk_the_guardian.txt',
    'uk_mail_news/uk_mail_news.txt',
]

ca_filenames = [
    'ca_cbc_news/ca_cbc_news.txt',
    'ca_ctv_news/ca_ctv_news.txt',
    'ca_global_news/ca_global_news.txt',
]

tw_filenames = [
    'tw_yahoo_news/tw_yahoo_news.txt',
    'tw_ettoday_news/tw_ettoday_news.txt',
    'tw_tvbs_news/tw_tvbs_news.txt',
]

au_filenames = [
    'au_news.com/au_news.com.txt',
    'au_abc_news/au_abc_news.txt',
    'au_nine_news/au_nine_news.txt',
]

jp_filenames = [
    #'jp_nhk.txt',
    'jp_yahoo_news/jp_yahoo_news.txt',
]

def squeeze(country):
    wf = open(f'all_{country}_news.txt', 'w')
    if country == 'uk':
        filenames = uk_filenames
    elif country == 'us':
        filenames = us_filenames
    elif country == 'ca':
        filenames = ca_filenames
    elif country == 'tw':
        filenames = tw_filenames
    elif country == 'au':
        filenames = au_filenames
    elif country == 'jp':
        filenames = jp_filenames

    for filename in filenames:
        rf = open(filename, 'r')
        line_count = 0
        line = rf.readline()
        while line:
            line_count += 1
            wf.write(line)
            line = rf.readline()
        rf.close()
        print(f'read {line_count} news from {filename}')
    wf.close()


country = sys.argv[1]

if __name__ == '__main__':
    if country == 'us':
        squeeze('us')
    elif country == 'uk':
        squeeze('uk')
    elif country == 'ca':
        squeeze('ca')
    elif country == 'tw':
        squeeze('tw')
    elif country == 'au':
        squeeze('au')
    elif country == 'jp':
        squeeze('jp')
    else:
        print(f'not supoorting {country}')
        pass
