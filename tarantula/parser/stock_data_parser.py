#!/usr/bin/python3
from basic_util.log import dlog, Log
from finance_model.stock_list import stock_code_decoding, index_code_decoding
from libutils.utils import drop_space
from libsql_utils.model.stock import get_formStock, formStockManager
from pandas import DataFrame
from sqlalchemy.orm import Session

def stock_name_parser(df):
    stock_id = df.iloc[0,0]
    stock_id = stock_code_decoding(stock_id)
    stock_name = drop_space(df.iloc[0,1])
    return stock_id, stock_name

def index_name_parser(df):
    stock_id = df.iloc[0,0]
    stock_id = index_code_decoding(stock_id)
    stock_name = drop_space(df.iloc[0,1])
    return stock_id, stock_name

@dlog
def stock_data_parser(engine, stock_code: str, df: DataFrame):
    formStock = get_formStock(stock_code)
    with Session(engine) as session:
        with session.begin():
            for index, row in df.iterrows():
                session.merge(
                    formStock(
                    trade_date=index,
                    stock_name=row["stock_name"],
                    close_price=row["close_price"],
                    high_price=row["high_price"],
                    low_price=row["low_price"],
                    open_price=row["open_price"],
                    prev_close_price=row["prev_close_price"],
                    change_rate=row["change_rate"],
                    amplitude=row["amplitude"],
                    volume=row["volume"],
                    turnover=row["turnover"],
                    )
                )
                update = index
            session.query(formStockManager).filter(formStockManager.stock_code==stock_code).update({"update_date": update})
            session.commit()


# import datetime
# from pandas import DataFrame

# d = [
#     {"trade_date": datetime.date(2021, 1, 1), "stock_code": 'SH600000', "stock_name": 'PFYH'},
#     {"trade_date": datetime.date(2021, 1, 2), "stock_code": 'SH600000', "stock_name": 'PFYH'},
#     {"trade_date": datetime.date(2021, 1, 3), "stock_code": 'SH600000', "stock_name": 'PFYH'},
# ]

# df = DataFrame(d)
# df.set_index('trade_date', inplace=True)
# print(df)
# stock_id = df.iloc[0,0]
# stock_name = df.iloc[0,1]
# print(stock_id)
# print(stock_name) 