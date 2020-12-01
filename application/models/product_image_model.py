from application import db

class ProductImageModel(db.Model):
    __tablename__ = 'product_images'

    row = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(100), db.ForeignKey('products.id'), nullable=False)
    image = db.Column(db.String(150), nullable=False)