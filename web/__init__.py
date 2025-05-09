from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
import os

# give permision to check the enviornment file key values
load_dotenv()

# initialize the flask server
app = Flask(__name__)

# configuration of the database with the server
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Cross-Origin-Resources Site 
# help to set the secure site fetching data
CORS(app, resoruces={r"/*": {
  "origins": ['http://localhost:3000'],
  "supports_credentials": True,
  "methods": ["GET", "POST", "PUT", "DELETE", "PATCH"],
  "allow_headers": ["Content-Type", "Authorization"]
}})

db = SQLAlchemy(app)

# initalize the bcrypt class
bcrypt = Bcrypt(app)

from web.routes import item_routes, user_routes, like_routes