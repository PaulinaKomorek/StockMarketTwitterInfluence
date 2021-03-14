from utilities.interpolation import interpolate, reverse_interpolate_date


def set_tweets_prices(tweets: list, prices: list):
    for tweet in tweets:
        if tweet.time < prices[0].time or tweet.time > prices[-1].time:
            continue
        for i in range(0, len(prices)):
            if tweet.time > prices[i].time and tweet.time < prices[i+1].time:
                dates_delta = reverse_interpolate_date(
                    tweet.time, prices[i].time, prices[i+1].time)
                price = interpolate(
                    dates_delta, prices[i].low, prices[i+1].low)
                tweet.price = price
                break
