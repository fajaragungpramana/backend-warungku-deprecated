from application import db

class VerificationModel(db.Model):
    __tablename__ = 'verifications'

    row = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.String(100), db.ForeignKey('owners.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    account = db.Column(db.String(30), nullable=False)
    email = db.Column(db.Boolean, default=False, nullable=False)
    phone = db.Column(db.Boolean, default=False, nullable=False)
    code = db.Column(db.Integer)