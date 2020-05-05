from datetime import datetime, timedelta
import json
import subprocess
import sys
import warnings

import requests
from newspaper import Article

API_KEY_LIST = [
    'xwrfuPbZBp2DPeGtEh2GUP-Fn82NTfV1PSHie_lovRA', # r07
]

AVAILABLE_NEWS_SOURCES = [
    # AU
    'abc',
    'news.com',
    'nine_news',
    # CA
    'cbc',
    'global',
    'ctv',
    # US
    'cnn',
    'foxnews',
    'huffpost',
    'nytimes',
    # UK
    'mail_news',
    'bbc',
    'the_guardian',
    # TW
    'yahoo_tw',
    'ettoday',
    'tvbs',
    # JP
    'yahoo_jp',
]

AVAILABLE_COUNTRIES = [
    'us',
    'uk',
    'ca',
    'au',
    'tw',
    'jp',
]

NEWS_SOURCES_BY_COUNTRY = {
    'us': ['cnn', 'foxnews', 'huffpost', 'nytimes'],
    'uk': ['mail_news', 'bbc', 'the_guardian'],
    'au': ['abc', 'news.com', 'nine_news'],
    'ca': ['cbc', 'global', 'ctv'],
    'tw': ['yahoo_tw', 'ettoday', 'tvbs'],
    'jp': ['yahoo_jp'],
}

PATH = {
    'abc': 'au_abc_news',
    'news.com': 'au_news.com',
    'nine_news': 'au_nine_news',
    'cbc': 'ca_cbc_news',
    'global': 'ca_global_news',
    'ctv': 'ca_ctv_news',
    'cnn': 'us_cnn_news',
    'foxnews': 'us_foxnews',
    'huffpost': 'us_huffpost',
    'nytimes': 'us_nytimes',
    'mail_news': 'uk_mail_news',
    'bbc': 'uk_bbc_news',
    'the_guardian': 'uk_the_guardian',
    'yahoo_tw': 'tw_yahoo_news',
    'ettoday': 'tw_ettoday_news',
    'tvbs': 'tw_tvbs_news',
    'yahoo_jp': 'jp_yahoo_news',
}

cmd = sys.argv[1]
news_source = sys.argv[2]
start_date = sys.argv[3]

if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    if cmd not in ['scrape', 'check', 'process']:
        print('invalid cmd')
    elif news_source not in AVAILABLE_NEWS_SOURCES + AVAILABLE_COUNTRIES:
        print(f'invalid news source {news_source}')
    elif news_source in AVAILABLE_NEWS_SOURCES:
        print(f'Processing {cmd} on {PATH[news_source]}')
        r = subprocess.run(['python3.8', f'{PATH[news_source]}/scrapeulous.py', cmd, start_date], capture_output=True)
        print(r)
    elif news_source in AVAILABLE_COUNTRIES:
        sources = NEWS_SOURCES_BY_COUNTRY[news_source]
        for source in sources:
            print(f'Processing {cmd} on {PATH[source]}')
            r = subprocess.run(['python3.8', f'{PATH[source]}/scrapeulous.py', cmd, start_date], capture_output=True)
            print(r)
