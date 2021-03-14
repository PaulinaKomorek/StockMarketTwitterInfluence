class Form:
    company: str
    user: str
    days: int

    def __init__(self, company, user, days):
        self.company = company
        self.user = user
        self.days = days
