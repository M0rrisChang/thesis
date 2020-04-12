import sys

us_filenames = [
    'cnn_news_us.txt',
    'foxnews_us.txt',
    'huffpost_us.txt',
    'nytimes_us.txt',
]

uk_filenames = [
    'bbc_news_uk.txt',
    'the_guardian_uk.txt',
    'mail_news_uk.txt',
]


def squeeze(country):
    wf = open(f'all_{country}_news.txt', 'w')
    if country == 'uk':
        filenames = uk_filenames
    elif country == 'us':
        filenames = us_filenames

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
    else:
        pass
