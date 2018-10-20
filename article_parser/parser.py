import requests
from article_parser.config import config
from newspaper import Article
import os.path


def get_news_url(url, parse_url, headers=None, params=None):
    if not url:
        raise Exception('There is no Url')
    req = requests.get(url=url, headers=headers, params=params)
    if not req.ok:
        raise Exception('Invalid request', req.text)

    for news_url in parse_url(req.text):
        yield news_url


def get_article_content(url):
    try:
        article = Article(url, language='ko')
        article.download()
        article.parse()
        text = article.text
    except Exception:
        text = ''
    return text


def write_article(content, file_dir):
    if os.path.exists(file_dir):
        fp = open(file_dir, 'a')
    else:
        fp = open(file_dir, 'w')
    if content:
        fp.write(content)
    fp.close()


def write_article_for_keywords(keyword, file_name, media):
    if not keyword:
        raise Exception('invalid keyword')
    if not file_name:
        raise Exception('invalid file name')

    if file_name.find('.txt') != len(file_name) - 4:
        file_name += '.txt'
    dir_name = '../dist/test'
    file_dir = os.path.join(dir_name, file_name)

    if type(media) is str:
        try:
            media = next(filter(lambda x: x['name'] == media, config))
        except Exception:
            raise Exception('there is no media {}'.format(media))

    params = media['params'].copy()
    params[media['keyword_params']] = keyword
    for news_url in get_news_url(media['url'], media['parse_url'],
                                 headers=media.get('headers', None), params=params):
        write_article(get_article_content(news_url),
                      file_dir)
    return '{}/{}'.format(dir_name, file_name)


def write_article_from_media(keyword, file_name):
    for media in config:
        file_dir = write_article_for_keywords(keyword, file_name, media)
        print('-' * 6 + 'finish' + '-' * 6)
        print('You can find \'{} news\' file in {}'.format(media['name'], file_dir))

