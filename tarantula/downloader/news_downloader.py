#!/usr/bin/python3
# file: tarantula/downloader/news_downloader.py

import requests
from basic_util.log import dlog
from .utils import SpiderMeta, get_html
from ..utils.headers import UserHeaders

class NENewsSpider(SpiderMeta):
    """
    下载新闻页面用于新闻解析
    """
    @dlog
    def download(self, url: str, headers):
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            html = get_html(resp)
        else:
            html = None
        return html
