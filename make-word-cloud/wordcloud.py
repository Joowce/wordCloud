from pytagcloud import create_html_data, create_tag_image,\
    make_tags, LAYOUT_HORIZONTAL
import os.path
from string import Template


def make_html_data(tag_count, file_name, font_max_size=120, html_size=(900, 600)):
    tag_list = make_tags(tag_count, maxsize=font_max_size)
    data = create_html_data(tag_list, size=html_size, layout=LAYOUT_HORIZONTAL, fontname='Korean')
    template_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'web/template.html'), 'r')
    html_template = Template(template_file.read())

    context = {}

    tags_template = '<li class="cnt" style="top: %(top)dpx; left: %(left)dpx; height: %(height)dpx;"><a class="tag %(cls)s" href="#%(tag)s"\
            style="top: %(top)dpx;left: %(left)dpx; font-size: %(size)dpx; height: %(height)dpx; line-height:%(lh)\
            dpx;">%(tag)s</a></li>'

    context['tags'] = ''.join([tags_template % link for link in data['links']])
    context['width'] = data['size'][0]
    context['height'] = data['size'][1]
    context['css'] = "".join("a.%(cname)s{color:%(normal)s;}\
            a.%(cname)s:hover{color:%(hover)s;}" %
                             {'cname': k,
                              'normal': v[0],
                              'hover': v[1]}
                             for k, v in data['css'].items())

    html_text = html_template.substitute(context)

    html_file = open(os.path.join('../dist', file_name), 'w')
    html_file.write(html_text)
    html_file.close()


def make_image(tag_count, file_name, font_max_size=120, size=(900, 600)):
    tag_list = make_tags(tag_count, maxsize=font_max_size)
    create_tag_image(tag_list, file_name, size=size,
                     fontname='Korean', rectangular=False)
    print("-" * 6 + "make wordcloud Image" + "-" * 6)
