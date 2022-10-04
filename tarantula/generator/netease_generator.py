#!/usr/bin/python3
import requests
from .generator_utils import GeneratorMeta
import datetime
from ..utils.headers import get_headers
import random
from redis import StrictRedis

# Generator将req_set通过redis传递给downloader

class StockGenerator(GeneratorMeta):
    def __init__(self) -> None:
        # 获取headers
        self.headers = get_headers()
        
    def run(self, stock_list):
        # 创建url generator
        req_set = []
        start_date = '19901219'
        end_date = datetime.date.today().strftime('%Y%m%d')
        req_set = (f"http://quotes.money.163.com/service/chddata.html?code={stock}&start={start_date}&end={end_date}&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER" for stock in stock_list )
        return req_set
    
    def set_value(self, value):
        s = StrictRedis(db=1, decode_responses=True)
        for item in value:
            s.lpush('cache_url', item)
        # 24h
        H24 = 3600 * 24
        s.expire('cache_url', H24)


