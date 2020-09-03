from StockMarketService import StockMarketService
from TwitterService import TwitterService
import matplotlib.pyplot as plt
from datetime import datetime


def on_plot_hover(event):
    for curve in plot.get_lines():
        contains, data = curve.contains(event)
        if contains:
            if curve.get_gid() == "tweets":
                annot.set_visible(True)
                tweet_id = data["ind"][0]
                annot.set_text(tweets[tweet_id][1])
                annot.set_position((tweets[tweet_id][0], 400))
                print(tweets[tweet_id][1])
            else:
                annot.set_visible(False)
    fig.canvas.draw()
  


fig, plot = plt.subplots()
sms = StockMarketService("TSLA")
prices = sms.get(10)
ts = TwitterService("elonmusk")
tweets = ts.get_tweets(10)
plot.plot(list(map(lambda x: x[0], prices)), list(map(lambda x: x[1], prices)))
plot.plot(list(map(lambda x: x[0], tweets)), [
          400]*len(tweets), "o", color="pink", gid="tweets")
annot = plt.annotate("", xy=(datetime.today(), 400))
annot.set_visible(False)

fig.canvas.mpl_connect('motion_notify_event', on_plot_hover)
plt.xticks(rotation=45)
plt.show()
