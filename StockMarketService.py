import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
from datetime import datetime, timedelta
from models.Price import Price

class StockMarketService():
    index_name: str


    def __init__(self, index_name: str):
        self.index_name = index_name

    def validate(self):
        try:
            self.get(1)
            return True
        except:
            return False
                

    def get(self, days: int):
        start_date = (datetime.today() - timedelta(days=days)).strftime("%Y-%m-%d")
        end_date = datetime.today().strftime("%Y-%m-%d")
        company_data = YahooFinancials(self.index_name)
        market_data = company_data.get_historical_price_data(start_date, end_date, 'daily')
        return list(map(lambda x: Price(datetime.strptime(x["formatted_date"], "%Y-%m-%d") , round(x["low"], 2), round(x["high"], 2)), market_data[self.index_name]["prices"]))
