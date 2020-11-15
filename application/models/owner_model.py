from application import db
from sqlalchemy import Column, Integer, String
from application.utils import date_now, get_ip_address, get_unique_id


# Database owner model schema
class OwnerModel(db.Model):
    __tablename__ = 'owners'

    raw = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String(100), unique=True, nullable=False, default=get_unique_id())
    photo = Column(String(100), unique=True)
    full_name = Column(String(50), nullable=False)
    address = Column(String(150))
    password = Column(String(100), nullable=False)
    create_at = Column(String(30), default=date_now())  # 15 Nov 2020 11:17:00
    update_at = Column(String(30), default=date_now())  # 15 Nov 2020 11:17:00
    ip_address = Column(String(30), default=get_ip_address())

    def __repr__(self):
        return '<OwnerModel {}>'.format(self.full_name)
