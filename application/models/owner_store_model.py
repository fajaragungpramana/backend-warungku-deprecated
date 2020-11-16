from sqlalchemy import Column, Integer, String, ForeignKey

from application import db
from .owner_model import OwnerModel

# Database owner store model schema
class OwnerStoreModel(db.Model):
    __tablename__ = 'owners_store'

    row = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(String(100), ForeignKey(OwnerModel.id), nullable=False)
    name = Column(String(50), nullable=False)
    address = Column(String(150), nullable=False)
    latitude = Column(String(50))
    longitude = Column(String(50))

    def __repr__(self):
        return '<OwnerStoreModel {}>'.format(self.name)