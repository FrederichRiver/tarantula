#!/usr/bin/python3
import datetime
from redis import StrictRedis
from .generator_utils import GeneratorMeta

# Generator将req_set通过redis传递给downloader

class StockGenerator(GeneratorMeta):
    """
    run方法生成urls
    set_value方法将urls写入redis数据库
    """       
    def run(self, stock_list):
        # 创建url generator
        start_date = '19901219'
        end_date = datetime.date.today().strftime('%Y%m%d')
        req_set = (f"http://quotes.money.163.com/service/chddata.html?code={stock}&start={start_date}&end={end_date}&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER" for stock in stock_list )
        return req_set
    
    def set_value(self, value, db=1, key='cache_url'):

        s = StrictRedis(db=db, decode_responses=True)
        for item in value:
            s.lpush(key, item)
        # expire time set to 22h
        H24 = 3600 * 22
        s.expire(key, H24)

class StockDataGenerator(GeneratorMeta):
      
    def run(self, stock_list, end_date: str, start_date='19901219'):
        # 创建url generator
        req_set = []
        for stock, stock2 in stock_list:
            req_set.append({"stock_code": stock, "stock_code2": stock2, "url":f"http://quotes.money.163.com/service/chddata.html?code={stock2}&start={start_date}&end={end_date}&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER" })
        return req_set
    
    def set_value(self, value, db=2, key='cache_url'):
        s = StrictRedis(db=db, decode_responses=True)
        for item in value:
            s.hmset(item["stock_code"], {"stock_code": item["stock_code"], "stock_code2": item["stock_code2"], "url": item["url"]})
        # expire time set to 22h
        H24 = 3600 * 22
        s.expire(key, H24)
