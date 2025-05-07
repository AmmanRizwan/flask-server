from web import db

class Item(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(100), unique=True, nullable=False)
  price = db.Column(db.Integer(), default=0, nullable=False)