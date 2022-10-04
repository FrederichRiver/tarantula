

def generate_url():
    from .netease_generator import StockGenerator
    stock_list = (f"060000{i}" for i in range(10))
    g = StockGenerator()
    r = g.run(stock_list)
    g.set_value(r)

if __name__ == '__main__':
    from .netease_generator import StockGenerator
    stock_list = (f"060000{i}" for i in range(10))
    g = StockGenerator()
    r = g.run(stock_list)
    g.set_value(r)