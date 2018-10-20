import sys
import os
from makeWordcloud.wordcloud import make_image
from makeWordcloud.morpheme import get_tags
from article_parser.parser import write_article_from_media


def main(argv):
    if len(argv) != 4:
        print('python mkWordcloud.py "keyword" "noun_count" "output_file_name"')
    keyword = argv[1]
    noun_count = int(argv[2])
    output_file_name = argv[3]

    temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist/temp.txt')
    result_dir = '/result/{}'.format(output_file_name)

    write_article_from_media(keyword, temp_dir)

    fp = open(temp_dir, 'r')
    text = fp.read()
    tags = get_tags(text, keyword, noun_count)
    fp.close()
    # os.remove(temp_dir)

    make_image(tags, result_dir)


if __name__ == '__main__':
    main(sys.argv)

