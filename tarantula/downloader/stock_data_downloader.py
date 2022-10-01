#!/usr/bin/python3

from .utils import SpiderMeta, get_excel


# 从网易财经获取股票日交易数据csv文件，生成DataFrame数据交给后续使用。

class StockDataDownloader(SpiderMeta):
    def download(self, url: str, header):
        df = get_excel(url)
        return df

# 从网易财经获取股票日交易数据csv文件，用于保存。

class StockDetailDataDownloader(SpiderMeta):
    def download(self):
        pass