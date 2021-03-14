import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
from datetime import datetime, timedelta
from models.Price import Price

class StockMarketService():
    index_name: str
    days: int
    

    def validate(self):
        try:
            self.days = 1
            self.get()
            return True
        except:
            return False
                

    def get(self):
        start_date = (datetime.today() - timedelta(days=self.days)).strftime("%Y-%m-%d")
        end_date = datetime.today().strftime("%Y-%m-%d")
        company_data = YahooFinancials(self.index_name)
        market_data = company_data.get_historical_price_data(start_date, end_date, 'daily')
        return list(map(lambda x: Price(datetime.strptime(x["formatted_date"], "%Y-%m-%d") , round(x["low"], 2), round(x["high"], 2)), market_data[self.index_name]["prices"]))
