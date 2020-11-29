from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize and set configuration database with flask
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
mail = Mail(app)

from .models.owner_model import OwnerModel
from .models.store_model import StoreModel
from .models.verification_model import VerificationModel
from .models.tip_model import TipModel