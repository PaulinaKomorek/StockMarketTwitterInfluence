import GetOldTweets3 as got
from datetime import datetime, timedelta

class TwitterService():
    user_name: str


    def __init__(self, user_name: str):
        self.user_name = user_name
    
    def get_tweets(self, days: int):
        start_date = (datetime.today() - timedelta(days=days)).strftime("%Y-%m-%d")
        end_date = datetime.today().strftime("%Y-%m-%d")
        tweets_criteria = got.manager.TweetCriteria().setUsername(self.user_name).setSince(start_date).setUntil(end_date)
        tweets = got.manager.TweetManager.getTweets(tweets_criteria)
        return list(map(lambda x: (datetime.strptime(x.date.strftime("%Y-%m-%d"), "%Y-%m-%d"), x.text, x.permalink), tweets))
