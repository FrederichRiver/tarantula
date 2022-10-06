#!/usr/bin/python3
# file: tarantula/downloader/news_downloader.py

import requests
from .utils import SpiderMeta, get_html
from ..utils.headers import UserHeaders

class NENewsSpider(SpiderMeta):
    """
    下载新闻页面用于新闻解析
    """
    def download(self, url: str, headers):
        resp = requests.get(url, headers=headers)
        html = get_html(resp)
        return html
