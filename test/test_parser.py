from article_parser.parser import get_news_url, write_article_for_keywords, write_article_from_media
from article_parser.config import config
import requests
import pytest


def test_get_news_url():
    test_keywords = '개헌'
    test_file_name = 'test'
    test_url = \
        'https://search.daum.net/search?w=news&nil_search=btn' +\
        '&DA=STC&enc=utf8&cluster=y&cluster_page=1&q=%EA%B0%9C%ED%97%8C'
    for url in get_news_url(test_url, config[1]['parse_url']):
        assert url is not None

    with pytest.raises(Exception):
        for url in get_news_url(None, config[1]['parse_url']):
            print(url)

    with pytest.raises(Exception):
        for url in get_news_url('~~~', config[1]['parse_url']):
            print(url)


def test_parse_url():
    test_url = \
        'https://search.daum.net/search?w=news&nil_search=btn' + \
        '&DA=STC&enc=utf8&cluster=y&cluster_page=1&q=%EA%B0%9C%ED%97%8C'
    test_req = requests.get(test_url)
    text = test_req.text
    generator = config[1]['parse_url'](text)
    for url in generator:
        assert url is not None


def test_write_article_for_keywords():
    test_file_name = 'pytest'
    test_key_word = '개헌'
    test_media = 'naver'
    assert write_article_for_keywords(test_key_word, test_file_name, test_media)
    assert write_article_for_keywords(test_key_word, 'daum_test', 'daum')

    with pytest.raises(Exception):
        write_article_for_keywords(test_key_word, test_file_name, 'google')

    with pytest.raises(Exception):
        write_article_for_keywords('', test_file_name, 'google')

    with pytest.raises(Exception):
        write_article_for_keywords(test_key_word, '', 'google')


def test_media():
    assert write_article_from_media('개헌', 'final_test')


