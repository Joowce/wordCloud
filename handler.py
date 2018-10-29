import json
import datetime
import boto3
import os
from make_word_cloud.wordcloud import make_image
from make_word_cloud.morpheme import get_tags
from article_parser.parser import write_article_from_media


def upload_to_s3(file_name):
    output_bucket_name = os.environ['bucket-name']
    tmp_file_dir = "/tmp/{}".format(file_name)

    s3 = boto3.resource('s3')
    bucket = s3.bucket(output_bucket_name)
    bucket.upload_file(tmp_file_dir, file_name)
    return file_name


def handler(event, context):
    keyword = event['keyword']
    noun_count = event.get('noun_count', 50)

    result = dict()

    if keyword is None:
        result.status = False
        result.message = 'You must contain Keyword'
        return json.dump(result)

    dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_file_name = "{}-{}.png".format(dt, keyword)
    tmp_file_dir = "/tmp/{}".format(output_file_name)

    temp_article_dir = "/tmp/{}-{}.txt".format(dt, keyword)
    write_article_from_media(keyword, temp_article_dir)

    fp = open(temp_article_dir, 'r')
    text = fp.read()
    tags = get_tags(text, keyword, noun_count)
    fp.close()
    os.remove(temp_article_dir)

    make_image(tags, tmp_file_dir)
    upload_to_s3(output_file_name)

    result.status = True
    result['fileName'] = output_file_name
    return result






