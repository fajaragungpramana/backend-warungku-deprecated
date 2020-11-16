from application import db


# Database owner store model schema
class StoreModel(db.Model):
    __tablename__ = 'stores'

    row = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.String(100), db.ForeignKey('owners.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(150))
    latitude = db.Column(db.String(50))
    longitude = db.Column(db.String(50))

    def __repr__(self):
        return '<StoreModel {}>'.format(self.name)
