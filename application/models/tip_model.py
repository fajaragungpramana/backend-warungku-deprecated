from application import db
from application.utils import date_now

class TipModel(db.Model):
    __tablename__ = 'tips'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(150), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.Text, nullable=False)
    create_at = db.Column(db.String(30), default=date_now())