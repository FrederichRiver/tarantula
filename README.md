# tarantula

A spider.

## 架构

Spider：要开发的爬虫程序，用来定义网站入口，实现解析逻辑并发起请求。
Pipeline：数据管道，可自定义实现数据持久化方式。
Middleware：中间件，分为两类。一类是下载器中间件，主要处理请求，用于添加请求头、代理等；一类是spider中间件，用于处理响应，用的很少。
Scheduler：调度器，用来存放爬虫程序的请求。
Downloader：下载器。对目标网站发起请求，获取响应内容。

## Work

1. 创建一个url生成器
2. 构建python到redis的接口，用于将url存储到redis当中
3. 构建一个scheduler，从redis当中读取url并分配给爬虫用于爬取
4. downloader，下载器
5. middleware中间件开发。

## 功能

### StockDataDownloader

### DetailStockDataDownloader

### CompanyinfoDownloader

### US/HK stock downloader

### Shibor data downloader

### GDP/PPI/CPI data downloader

### News Downloader

