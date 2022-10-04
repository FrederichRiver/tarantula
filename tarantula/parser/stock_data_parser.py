

def stock_name_parser(df):
    stock_id = df.iloc[0,0]
    stock_name = df.iloc[0,1]
    return stock_id, stock_name

def stock_data_parser(df):
    pass

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