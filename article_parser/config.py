from scrapy import Selector
import json


def parse_url(text):
    for item in Selector(text=text).xpath('//*[@id="clusterResultUL"]/li'):
        yield item.xpath('div[@class="wrap_cont"]/div[@class="cont_inner"]/div[@class="wrap_tit mg_tit"]/a/@href')\
            .extract()[0]


def parse_url_naver(text):
    res = json.loads(text, encoding='utf-8')
    if not res.get('items'):
        raise Exception('Invalid response', 'There is no Items in response')
    for item in res['items']:
        if not item.get('link'):
            raise Exception('Invalid response', 'There is no link in response')
        yield item['link']


naver = {
    'name': 'naver',
    'headers': {
        'X-Naver-Client-Id': 'lumOzzvDGqgyIViSi8Bo',
        'X-Naver-Client-Secret': 'Ze33bmH4fw',
    },
    'url': 'https://openapi.naver.com/v1/search/news.json',
    'params': {
        'display': 10
    },
    'keyword_params': 'query',
    'parse_url': parse_url_naver
}
daum = {
    'name': 'daum',
    'url': 'https://search.daum.net/search',
    'params': {
        'w': 'news',
        'nil_search': 'btn',
        'DA': 'PGD',
        'enc': 'utf8',
        'cluster': 'y',
        'cluster_page': '1',
    },
    'keyword_params': 'q',
    'parse_url': parse_url
}

config = [naver, daum]

