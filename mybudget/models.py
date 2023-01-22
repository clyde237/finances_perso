from app import db


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    amount = db.Column(db.Float)
    category = db.Column(db.String(64))
    date = db.Column(db.DateTime)
    account = db.Column(db.String(64))

    def __init__(self, name, amount, category, date, account):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date
        self.account = account

    def __repr__(self):
        return '<Expense {}>'.format(self.name)


class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    amount = db.Column(db.Float)
    category = db.Column(db.String(64))
    date = db.Column(db.DateTime)
    account = db.Column(db.String(64))

    def __init__(self, name, amount, category, date, account):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date
        self.account = account

    def __repr__(self):
        return '<Income {}>'.format(self.name)
