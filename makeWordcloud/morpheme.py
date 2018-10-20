from konlpy.tag import Twitter
from collections import Counter


def get_tags(text, keyword, tags=50):
    spliter = Twitter()
    # print(text[0])
    nouns = spliter.nouns(text)
    count = Counter(nouns)
    del count[keyword]
    print('-' * 6 + 'morpheme finish' + '-' * 6)
    return count.most_common(tags)
