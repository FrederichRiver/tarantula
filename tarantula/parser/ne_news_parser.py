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
Regx1 = re.compile(r'\S*/money/article/\S*.html')
Regx2 = re.compile(r'\S*/dy/article/\S*.html')
Regx3 = re.compile(r'\S*/money.163.com/\d{2}/\d{4}/\d{2}/\S*.html')
Regx4 = re.compile(r'\S*/money.163.com/(special|fund|chanjing|yihuiman|ipo|stock)')
Regx5 = re.compile(r'\S*/dy/article/\S*.html')

"""
网易公开课
vip.open.163.com/courses/xxx
网易财经
/money.163.com/
/www.163.com/money/article/
网易手机财经
i.money.163.com
网易大鱼媒体
www.163.com/dy/media
网易视频
www.163.com/v/video
网易旅游频道
travel.163.com

"""

def ne_news_parser(rds: StrictRedis, html):
    """
    解析来自www.163.com的网页，提取url并保存至redis数据库
    Oct 9进行更详细的频道分类
    """
    url_set = html.xpath('//a//@href')
    for url in url_set:
        if re.search(Regx1, url):
            # Regx1 = re.compile(r'\S*/money/article/\S*.html')
            url = concat_url(url)
            i = rds.sadd('article_page', url)
        elif re.search(Regx3, url):
            # Regx3 = re.compile(r'\S*/money.163.com/\d{2}/\d{4}/\d{2}/\S*.html')
            url = concat_url(url)
            i = rds.sadd('article_page', url)
        elif re.search(Regx5, url):
            # Regx3 = re.compile(r'\S*/dy/article/\S*.html')
            url = concat_url(url)
            i = rds.sadd('dy_page', url)
        elif re.search(Regx4, url):
            # Regx4 = re.compile(r'\S*/money.163.com/(special|fund|chanjing|yihuiman|ipo|stock)')
            url = concat_url(url)
            # send to news source
            i = rds.sadd("news_source", url)
        else:
            url = concat_url(url)
            i = rds.sadd("other_url", url)  

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


