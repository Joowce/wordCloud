from media.media import Media
import json


class Naver(Media):
    def __init__(self):
        Media.__init__(self,
                       name='naver',
                       headers={
                           'X-Naver-Client-Id': 'lumOzzvDGqgyIViSi8Bo',
                           'X-Naver-Client-Secret': 'Ze33bmH4fw'
                       },
                       url='https://openapi.naver.com/v1/search/news.json',
                       params={'display': 10}
                       )

    def parse_url(self, text):
        res = json.loads(text, encoding='utf-8')
        if not res.get('item'):
            raise Exception('Invalid response', 'There is no Items in response')
        for item in iter(res['item']):
            if not item.get('link'):
                raise Exception('Invalid response', 'There is no link in response')
            yield item['link']
