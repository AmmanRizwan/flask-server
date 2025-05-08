from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
import os

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app, resoruces={r"/*": {
  "origins": ['http://localhost:3000'],
  "supports_credentials": True,
  "methods": ["GET", "POST", "PUT", "DELETE", "PATCH"],
  "allow_headers": ["Content-Type", "Authorization"]
}})

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from web.routes import item_routes, user_routes