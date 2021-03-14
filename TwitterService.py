import twint 
from datetime import datetime, timedelta
from models.Tweet import Tweet

class TwitterService():
    user_name: str
    days: int


    def validate(self):
        try:
            self.days = 1
            self.get_tweets()
            return True
        except:
            return False
    
    def get_tweets(self):
        start_date = (datetime.today() - timedelta(days=self.days)).strftime("%Y-%m-%d")
        end_date = datetime.today().strftime("%Y-%m-%d")
        c = twint.Config()
        c.Username = self.user_name
        c.Since = start_date
        c.Until= end_date
        c.Store_object = True
        twint.run.Search(c)
        tweets = twint.output.tweets_list
        return list(map(lambda x: Tweet(datetime.strptime(x.datestamp, "%Y-%m-%d"), x.tweet, x.link), tweets))

