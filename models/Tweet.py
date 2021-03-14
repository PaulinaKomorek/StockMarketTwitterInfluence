import datetime


class Tweet:
    time: datetime.datetime
    content: str
    link: str
    price: float

    def __init__(self, time, content, link):
        self.time = time
        self.content = content
        self.link = link
