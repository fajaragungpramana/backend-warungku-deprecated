from application.utils import date_now, get_ip_address
from application import db


# Database owner model schema
class OwnerModel(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.String(100), primary_key=True, nullable=False)
    photo = db.Column(db.String(100))
    full_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(150))
    store = db.relationship('StoreModel', backref='owners')
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    verification = db.relationship('VerificationModel', backref='owners')
    create_at = db.Column(db.String(30), default=date_now())  # 15 Nov 2020 11:17:00
    update_at = db.Column(db.String(30), default=date_now())  # 15 Nov 2020 11:17:00
    ip_address = db.Column(db.String(30), default=get_ip_address())

    def __repr__(self):
        return '<OwnerModel {}>'.format(self.full_name)
