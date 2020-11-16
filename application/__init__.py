from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize and set configuration database with flask
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models.owner_model import OwnerModel
from .models.owner_store_model import OwnerStoreModel