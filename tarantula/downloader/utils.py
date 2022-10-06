#!/usr/bin/python3
import pandas as pd
import requests
from lxml import etree
from pandas import DataFrame

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

def get_csv(url, encode):
    df = pd.read_csv(url, encoding=encode)
    return df

def get_text(response):
    return response.text