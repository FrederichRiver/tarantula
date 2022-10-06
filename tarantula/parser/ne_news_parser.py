#!/usr/bin/python3
# file: tarantula/parser/ne_news_parser.py

import re
from redis import StrictRedis
from .parser_utils import text_clean

def concat_url(url):
    if url.startswith('http'):
        return url
    elif url.startswith('//'):
        url = 'https:' + url
        return url
    else:
        return ''

# 匹配网易article文章
Rex1 = re.compile(r'\S*article/\S*.html')

def ne_news_parser(html, rds):
    """
    解析来自www.163.com的网页，提取url并保存至redis数据库
    """
    rds = StrictRedis('localhost', db=4)
    url_set = html.xpath('//a//@href')
    for url in url_set:  
        if re.search('money.163.com', url):
            url = concat_url(url)
            # send to news source
            rds.lpush('news_source', url)
        elif re.search(Rex1, url):
            # send to article page
            url = concat_url(url)
            rds.lpush('article_page', url)
        # else:
        #     print(concat_url(url))

def ne_article_parser(html):
    title = get_title(html)
    post_time = get_post_time(html)
    content = get_content(html)
    return title, post_time, content




def get_title(html):
    title = html.xpath("//div/h1/text()")
    if title:
        title = text_clean(title[0])
    else:
        title = 'unknow title'
    return title

def get_content(html):
    """
    tag: //div[@class=post_body] for netease finance
    """
    html = html.xpath("//div[@class='post_body']/p//text()")
    content = r''
    for line in html:
        content += (line + '\n')
    content = content.strip()
    content = content.replace(' ', '')
    # content = content.replace('\n', '')
    return content

def get_post_time(html):
    regex_date = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    date_string = html.xpath("//div[@class='post_info']/text()")
    post_time = '1900-10-01 00:00:01'
    for s in date_string:
        if result := re.search(regex_date, s):
            post_time = result[0]
    return post_time
