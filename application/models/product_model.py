from application import db

class ProductModel(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.String(100), primary_key=True)
    owner_id = db.Column(db.String(100), db.ForeignKey('owners.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    weight_unit = db.Column(db.String(10), nullable=False)
    available = db.Column(db.Integer, nullable=False)
    available_unit = db.Column(db.String(10), nullable=False)
    minimal_order = db.Column(db.Integer, nullable=False)
    purchase_price = db.Column(db.BigInteger, nullable=False)
    sell_price = db.Column(db.BigInteger, nullable=False)
    profit_percentage = db.Column(db.String(10), nullable=False)
    description = db.Column(db.Text, nullable=False)
    barcode = db.Column(db.BigInteger, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    expired = db.Column(db.String(50), nullable=False)