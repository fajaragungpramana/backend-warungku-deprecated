from sqlalchemy import Column, Integer, String, ForeignKey

from application import db

# Database owner store model schema
class OwnerStoreModel(db.Model):
    __tablename__ = 'stores'

    row = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(String(100), ForeignKey('owners.id'), nullable=False)
    name = Column(String(50), nullable=False)
    address = Column(String(150), nullable=False)
    latitude = Column(String(50))
    longitude = Column(String(50))

    def __repr__(self):
        return '<OwnerStoreModel {}>'.format(self.name)