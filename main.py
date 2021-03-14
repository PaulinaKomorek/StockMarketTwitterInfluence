from StockMarketService import StockMarketService
from TwitterService import TwitterService
from DrawingService import DrawingService
from datetime import datetime, timedelta
from InputBox import InputBox
from utilities.set_tweets_prices import set_tweets_prices


def main():
    sms = StockMarketService()
    ts = TwitterService()
    InputBox(sms, ts)
    prices = sms.get()
    tweets = ts.get_tweets()
    set_tweets_prices(tweets, prices)
    tweets = list(filter(lambda x: hasattr(x, "price"), tweets))
    ds = DrawingService(tweets, prices)
    ds.draw()


if __name__ == "__main__":
    main()



