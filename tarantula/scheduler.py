from .downloader.stock_data_downloader import StockDataDownloader
from .utils.headers import get_headers
from redis import StrictRedis
import random

def schedule():
    s = StrictRedis(db=1, decode_responses=True)
    d = StockDataDownloader()
    h = get_headers()
    while url:=s.brpop('cache_url', 5):
        df = d.download(url[1])
        print(df.head(5))
        
schedule()
