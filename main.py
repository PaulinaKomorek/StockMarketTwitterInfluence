from StockMarketService import StockMarketService
from TwitterService import TwitterService
from DrawingService import DrawingService
from datetime import datetime, timedelta

sms = StockMarketService("TSLA")
prices = sms.get(5)
ts = TwitterService("elonmusk")
tweets = ts.get_tweets(5)

priced_tweets=[]

def reverse_interpolate_date(val: datetime, start: datetime, end: datetime):
    start_end_delta=(end-start).total_seconds()
    start_val_delta=(val-start).total_seconds()
    delta=start_val_delta/start_end_delta
    return delta 

def interpolate(delta: float, start: float, end: float):
    return start+(end-start)*delta

for tweet in tweets:
    if tweet[0]<prices[0][0] or tweet[0]>prices[-1][0]:
        continue
    for i in range(0, len(prices)):
        if tweet[0]>prices[i][0] and tweet[0]<prices[i+1][0]:
            dates_delta=reverse_interpolate_date(tweet[0], prices[i][0], prices[i+1][0])
            price=interpolate(dates_delta, prices[i][1], prices[i+1][1])
            priced_tweets.append((tweet[0], tweet[1], price, tweet[2]))
            break

ds=DrawingService(priced_tweets, prices)
ds.draw()
    

reverse_interpolate_date(datetime.today(), datetime.today()-timedelta(days=1), datetime.today()+timedelta(days=3))

