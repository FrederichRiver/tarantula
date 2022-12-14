#!/usr/bin/python3

import os
import pandas as pd
from pandas import DataFrame
from .utils import SpiderMeta

# 从网易财经获取股票日交易数据csv文件，生成DataFrame数据交给后续使用。

class StockDataDownloader(SpiderMeta):
    def download(self, url: str):
        col = [
            'trade_date', 'stock_code', 'stock_name', 'close_price',
            'high_price', 'low_price', 'open_price', 'prev_close_price',
            'change_rate', 'amplitude', 'volume', 'turnover']
        try:
            df = pd.read_csv(url, names=col, header=0, encoding='gb18030', parse_dates=True, na_values='None')
        except Exception as e:
            df = DataFrame()
        if not df.empty:
            df.set_index('trade_date', inplace=True)
        return df

# 从网易财经获取股票日交易数据csv文件，用于保存。


class StockDetailDataDownloader(SpiderMeta):
    file_path = '/home/fred/Downloads/tmp'
    def download(self, stock_code: str, url: str):
        col = []
        df = pd.read_excel(url, names=col, header=0, encoding='gb18030', parse_dates=True, na_values='None')
        if not df.empty:
            file_name = os.path.join(self.file_path, f"{stock_code}.csv")
            df.to_csv(file_name, encoding='gb18030')