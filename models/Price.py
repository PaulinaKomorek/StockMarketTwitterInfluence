import datetime

class Price:
    time: datetime.datetime
    low: float
    high: float

    def __init__(self, time, low, high):
        self.time = time
        self.low = low
        self.high = high