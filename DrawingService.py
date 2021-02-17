import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import webbrowser


class DrawingService():
    fig: plt.Figure
    plot: plt.Axes
    annot: plt.Text
    tweets: list
    prices: list

    def __init__(self, tweets: list, prices: list):
        self.tweets=tweets
        self.prices=prices
        self.fig, self.plot = plt.subplots()
        if len(tweets)>0:
            self.annot = plt.text(tweets[0][0]-timedelta(days=1), 400, "", backgroundcolor="white", wrap=True)
            self.annot.set_visible(False)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_plot_hover)
        self.fig.canvas.mpl_connect('button_press_event', self.on_plot_click)
        plt.xticks(rotation=45)


    def on_plot_hover(self, event):
        x, y = event.xdata, event.ydata
        for curve in self.plot.get_lines():
            contains, data = curve.contains(event)
            if contains and curve.get_gid() == "tweets":
                self.annot.set_visible(True)
                tweet_ids = data["ind"]
                tweets = list(map(lambda i: self.tweets[i][1], tweet_ids))
                self.annot.set_text("\n\n".join(tweets))
                self.annot.set_position((x, y))
            else:
                self.annot.set_visible(False)
                if x!=None and y!=None:
                    self.annot.set_position((x, y))
        self.fig.canvas.draw_idle()

    def on_plot_click(self, event):
        x, y = event.xdata, event.ydata
        for curve in self.plot.get_lines():
            contains, data = curve.contains(event)
            if contains and curve.get_gid() == "tweets":
                tweet_id = data["ind"][0]
                link=self.tweets[tweet_id][3]
                webbrowser.open(link, new=2)
               
 
  

    def draw(self):
        self.plot.plot(list(map(lambda x: x[0], self.prices)), list(map(lambda x: x[1], self.prices)))
        self.plot.plot(list(map(lambda x: x[0], self.tweets)), list(map(lambda x: x[2], self.tweets)), "o", color="pink", gid="tweets")
        plt.show()

