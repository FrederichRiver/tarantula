#!/usr/bin/python3
# tarantula/generator/news_generator.py

from redis import StrictRedis
from .generator_utils import GeneratorMeta

class NENewsGenerator(GeneratorMeta):
    """
    生成新闻网页入口，用于进一步获取url
    """
    def run(self) -> list:
        url_set = []
        # macro news channel
        url_set.append("http://money.163.com/special/00252G50/macro.html")
        url_set += [f"http://money.163.com/special/00252G50/macro_{str(i).zfill(2)}.html" for i in range(2, 21)]
        # internal news channel
        url_set.append("http://money.163.com/special/00252C1E/gjcj.html")
        url_set += [f"http://money.163.com/special/00252C1E/gjcj_{str(i).zfill(2)}.html" for i in range(2, 21)]
        # stock news channel
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_index.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_index_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # hk stock news channel
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_hkstock.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_hkstock_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # us stock news channel.
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_usstock.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_usstock_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # new stock news channel
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_ipo.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_ipo_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # future news channel
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_qhzx.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_qhzx_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # forexchange news channel
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_forex.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_forex_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # btc news channel
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_bitcoin.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_bitcoin_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # 科创板 news channel
        url_set.append("http://money.163.com/special/00259D2D/fund_newsflow_hot.js?callback=data_callback")
        url_set += [f"http://money.163.com/special/00259D2D/fund_newsflow_hot_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # fund news.
        url_set.append("http://money.163.com/special/00259CPE/data_kechuangban_kechuangban.js?callback=data_callback")
        url_set += [f"http://money.163.com/special/00259CPE/data_kechuangban_kechuangban_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # News about Chairman Yi Huiman.
        url_set.append("http://money.163.com/special/00259CTD/data-yihuiman.js?callback=data_callback")
        url_set += [f"http://money.163.com/special/00259CTD/data-yihuiman_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # Business channel.
        url_set.append("http://money.163.com/special/002557RF/data_idx_shangye.js?callback=data_callback")
        url_set += [f"http://money.163.com/special/002557RF/data_idx_shangye_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # Estate channel.
        url_set.append("http://money.163.com/special/002534NU/house2010.html")
        url_set += [f"http://money.163.com/special/002534NU/house2010_{str(i).zfill(2)}.html" for i in range(2, 21)]
        # auto news channel
        url_set.append("http://money.163.com/special/002534NV/auto_house.html")
        url_set += [f"http://money.163.com/special/002534NU/house2010_{str(i).zfill(2)}.html" for i in range(2, 21)]

        return url_set

    def set_value(self, value, db=3, key='ne_news_url', n=1):
        s = StrictRedis(db=db, decode_responses=True)
        for item in value:
            s.lpush(key, item)
        # expire time set to 22h
        H24 = 3600 * 22 * n
        s.expire(key, H24)

#     def extract_href(self, url):
#         """
#         From html page extract urls.
#         """
#         resp = requests.get(url)
#         if resp.status_code == 200:
#             result = re.findall(r'\"docurl\":\"(http.://money.163.com/\d{2}/\d{4}/\d{2}/\w+\.html)\"', resp.text)
#             self.href += result

#     @log_decorator
#     def extract_article(self, url):
#         art = article()
#         resp = requests.get(url)
#         if resp.status_code == 200:
#             h = lxml.etree.HTML(resp.text)
#             content = h.xpath("//div[@class='post_text']/p/text()")
#             art.url = url
#             art.title = art._get_title(h)
#             art.author = art._get_author(h)
#             art.date = art._get_date(h)
#             art.source = art._get_source(h)
#             content = h.xpath("//div[@class='post_text']/p")
#             art.content = art._text_clean(content)
#         else:
#             art = None
#         return art

#     @log_decorator2
#     def record_article(self, art):
#         insert_data = {
#             'title': f"{art.title}",
#             'url': f"{art.url}",
#             'release_date': f"{art.date}",
#             'author': f"{art.author}",
#             'source': f"{art.source}",
#             }
#         self.mysql.session.execute(
#             formArticle.__table__.insert().prefix_with('IGNORE'),
#             insert_data)
#         self.mysql.session.commit()
#         path = '/home/friederich/Downloads/news/'
#         filename = path + get_url_hash(art.url)
#         with open(filename, 'w') as f:
#             f.write(art.content)


class SinaNewsGenerator(GeneratorMeta):
    def run(self) -> list:
        url_set = []
        # macro news channel
        url_set.append("http://money.163.com/special/00252G50/macro.html")
        url_set += [f"http://money.163.com/special/00252G50/macro_{str(i).zfill(2)}.html" for i in range(2, 21)]
        # internal news channel
        url_set.append("http://money.163.com/special/00252C1E/gjcj.html")
        url_set += [f"http://money.163.com/special/00252C1E/gjcj_{str(i).zfill(2)}.html" for i in range(2, 21)]
        # stock news channel
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_index.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_index_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # hk stock news channel
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_hkstock.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_hkstock_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # us stock news channel.
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_usstock.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_usstock_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # new stock news channel
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_ipo.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_ipo_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # future news channel
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_qhzx.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_qhzx_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # forexchange news channel
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_forex.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_forex_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # btc news channel
        url_set.append("https://money.163.com/special/002557S6/newsdata_gp_bitcoin.js?callback=data_callback")
        url_set += [f"https://money.163.com/special/002557S6/newsdata_gp_bitcoin_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # 科创板 news channel
        url_set.append("http://money.163.com/special/00259D2D/fund_newsflow_hot.js?callback=data_callback")
        url_set += [f"http://money.163.com/special/00259D2D/fund_newsflow_hot_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # fund news.
        url_set.append("http://money.163.com/special/00259CPE/data_kechuangban_kechuangban.js?callback=data_callback")
        url_set += [f"http://money.163.com/special/00259CPE/data_kechuangban_kechuangban_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # News about Chairman Yi Huiman.
        url_set.append("http://money.163.com/special/00259CTD/data-yihuiman.js?callback=data_callback")
        url_set += [f"http://money.163.com/special/00259CTD/data-yihuiman_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # Business channel.
        url_set.append("http://money.163.com/special/002557RF/data_idx_shangye.js?callback=data_callback")
        url_set += [f"http://money.163.com/special/002557RF/data_idx_shangye_0{i}.js?callback=data_callback" for i in range(2, 10)]
        # Estate channel.
        url_set.append("http://money.163.com/special/002534NU/house2010.html")
        url_set += [f"http://money.163.com/special/002534NU/house2010_{str(i).zfill(2)}.html" for i in range(2, 21)]
        # auto news channel
        url_set.append("http://money.163.com/special/002534NV/auto_house.html")
        url_set += [f"http://money.163.com/special/002534NU/house2010_{str(i).zfill(2)}.html" for i in range(2, 21)]

        return url_set

    def set_value(self, value, db=3, key='sina_news_url'):
        s = StrictRedis(db=db, decode_responses=True)
        for item in value:
            s.lpush(key, item)
        # expire time set to 22h
        H24 = 3600 * 22
        s.expire(key, H24)


# class SinaNewsSpider(newsSpiderBase):
#     def start_url(self, count=1):
#         for i in range(count, count+10000):
#             self.url_list.append(f"http://roll.finance.sina.com.cn/finance/zq1/index_{i}.shtml")

#     def generate_url_list(self):
#         """
#         http://roll.finance.sina.com.cn/finance/zq1/index_1.shtml
#         https://finance.sina.com.cn/stock/
#         http://finance.sina.com.cn/stock/newstock/
#         http://finance.sina.com.cn/stock/hkstock/
#         https://finance.sina.com.cn/stock/usstock/
#         http://finance.sina.com.cn/stock/kechuangban/
#         http://finance.sina.com.cn/stock/quanshang/
#         http://finance.sina.com.cn/stock/estate/
#         https://finance.sina.com.cn/fund/
#         https://finance.sina.com.cn/futuremarket/
#         https://finance.sina.com.cn/forex/
#         https://finance.sina.com.cn/nmetal/
#         http://finance.sina.com.cn/bond/
#         http://finance.sina.com.cn/money/
#         http://finance.sina.com.cn/money/bank/
#         http://finance.sina.com.cn/money/insurance/
#         http://finance.sina.com.cn/trust/
#         http://finance.sina.cn/esg/
#         http://finance.sina.com.cn/meeting/
#         http://finance.sina.com.cn/zt_d/20200727dp/
#         https://finance.sina.cn/roll.d.html?rollCid=230808
#         http://stock.finance.sina.com.cn/stock/go.php/vReport_List/kind/lastest/index.phtml
#         http://finance.sina.com.cn/qizhi/
#         http://finance.sina.com.cn/7x24/
#         """
#         url = "https://finance.sina.com.cn/stock/"
#         return url

#     def extract_href(self, url: str) -> list:
#         resp = requests.get(url)
#         if resp.status_code == 200:
#             result = lxml.etree.HTML(resp.text)
#             urls = result.xpath("//li/a/@href")
#         else:
#             urls = []
#         result = []
#         for url in urls:
#             # if re.match(r'(http|https)://finance.sina.com.cn/(stock|roll|wm|dy)/\w+/\d{4}-\d{2}-\d{2}/doc-[0-9a-zA-Z]+.shtml', url):
#             if re.match(r'(http|https)://finance.sina.com.cn/[a-zA-Z0-9_/]+/\d{4}-\d{2}-\d{2}/doc-[0-9a-zA-Z]+.shtml', url):
#                 result.append(url)
#             elif re.match(r'(http|https)://finance.sina.com.cn/[a-zA-Z0-9_/]+/\d{8}/[0-9a-zA-Z]+.shtml', url):
#                 result.append(url)
#             else:
#                 with open('/home/friederich/Documents/spider/failed', 'a') as f:
#                     f.write(f"{url}\n")
#         return result

#         """
#         with open('/home/friederich/Documents/spider/urls2', 'w') as f:
#             line = ''
#             for url in result:
#                 line = url + '\n'
#                 f.writelines(line)
#         return result
#         """

#     def record_url(self, url):
#         """
#         Insert url into table natural_language.news
#         """
#         sql = f"INSERT IGNORE into news (url) values ('{url}')"
#         self.mysql.engine.execute(sql)

#     def extract_article(self, url: str) -> SinaArticle:
#         """
#         Extract article from finance@sina
#         """
#         resp = requests.get(url)
#         sina_article = SinaArticle()
#         if resp.status_code == 200:
#             html = lxml.etree.HTML(resp.text.encode('ISO-8859-1'))
#             sina_article.url = url
#             sina_article.title = sina_article._get_title(html)
#             sina_article.author = sina_article._get_author(html)
#             sina_article.date = sina_article._get_date(html)
#             sina_article.source = sina_article._get_source(html)
#             content_text = html.xpath("//div[@class='article']/p//text()")
#             content = sina_article._text_clean(content_text)
#             filename = self.path + get_url_hash(url)
#             self.save_file(filename, content)
#         return sina_article

#     def record_article(self, art):
#         query = self.mysql.session.query(formNews).filter_by(url=art.url).first()
#         query.title = art.title
#         query.release_date = art.date
#         query.author = art.author
#         query.source = art.source
#         query.filename = get_url_hash(art.url)
#         self.mysql.session.commit()


# def get_url_hash(url: str) -> str:
#     # url = 'http://www.baidu.com'
#     m = hashlib.md5()
#     m.update(url.encode('utf-8'))
#     urlhash = m.hexdigest()
#     return urlhash


# class newsSpider(StockBase):
#     def __init__(self, header) -> None:
#         super(newsSpider, self).__init__(header)
#         self.filepath = '/home/friederich/Downloads/page/'

#     def get_url_list(self) -> list:
#         query = self.condition_select('news', 'url', 'filename is null')
#         url_list = []
#         if not query.empty:
#             url_list = list(query[0])
#         return url_list

#     def save_page(self, url) -> None:
#         resp = requests.get(url)
#         filehash = get_url_hash(url)
#         filename = self.filepath + filehash + '.html'
#         if resp.status_code == 200:
#             with open(filename, 'w', encoding=resp.encoding) as f:
#                 f.write(resp.text)
#             self.record_page(filehash, url)
#         else:
#             self.record_page('failed', url)

#     def record_page(self, filename, url):
#         self.update_value('news', 'filename', f"'{filename}'", f"url='{url}'")

