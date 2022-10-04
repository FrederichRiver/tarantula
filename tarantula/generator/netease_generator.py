#!/usr/bin/python3
from .generator_utils import GeneratorMeta
import datetime
from ..utils.headers import get_headers
from redis import StrictRedis

# Generator将req_set通过redis传递给downloader

class StockGenerator(GeneratorMeta):
    """
    run方法生成urls
    set_value方法将urls写入redis数据库
    """
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
    
    def set_value(self, value, db=1, key='cache_url'):

        s = StrictRedis(db=db, decode_responses=True)
        for item in value:
            s.lpush(key, item)
        # expire time set to 22h
        H24 = 3600 * 22
        s.expire('cache_url', H24)


