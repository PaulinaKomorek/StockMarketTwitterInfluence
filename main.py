from StockMarketService import StockMarketService
from TwitterService import TwitterService
from DrawingService import DrawingService
from datetime import datetime, timedelta
from InputBox import InputBox
from utilities.set_tweets_prices import set_tweets_prices


def main():
    ib = InputBox()
    form = ib.get_data()
    sms = StockMarketService(form.company)
    while not sms.validate():
        ib = InputBox()
        form = ib.get_data()
        sms.index_name = form.company
    prices = sms.get(form.days)
    ts = TwitterService(form.user)
    while not ts.validate():
        ib = InputBox()
        form = ib.get_data()
        ts.user_name = form.user
    tweets = []
    tweets = ts.get_tweets(form.days)
    set_tweets_prices(tweets, prices)
    tweets = list(filter(lambda x: hasattr(x, "price"), tweets))
    ds = DrawingService(tweets, prices)
    ds.draw()


if __name__ == "__main__":
    main()


# znaleźć, jak się robi "słupki"-błąd
