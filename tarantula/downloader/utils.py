#!/usr/bin/python3
import requests
import datetime
from libutils.network import RandomHeader
from libutils.log import Log, method
from libutils.utils import trans
import pandas as pd
import re
import json
import numpy as np
import requests
from lxml import etree
from dev_global.env import TIME_FMT
from libmysql_utils.mysql8 import (mysqlBase, mysqlHeader, Json2Sql)
from pandas import DataFrame
from requests.models import HTTPError
from libmysql_utils.orm.form import formStockManager
from libbasemodel.cninfo import cninfoSpider
from sqlalchemy import exc
"""
共性工具
"""

class SpiderMeta(object):
    def get(self, url: str, header):
        """
        Return http response.
        """
        response = requests.get(url, headers=header)
        return response


def get_html(response) -> etree.HTML:
    """
    result is a etree.HTML object
    """
    # setting encoding
    response.encoding = response.apparent_encoding
    html = etree.HTML(response.text)
    return html

def get_excel(url) -> DataFrame:
    df = pd.read_excel(url, header=0, parse_dates=True)
    return df

def get_text(response):
    return response.text