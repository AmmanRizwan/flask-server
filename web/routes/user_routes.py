from flask import jsonify, request
from web import app, db
from web.model.User import User
from web import bcrypt
import uuid 
import re

@app.route("/api/users/all", methods=["GET"])
def allUser():
  users = User.query.all()
  if users is None:
    return jsonify({"error": "Cannot Find any user!"}), 404

  return jsonify([{"id": user.id, "username": user.username, "name": user.name, "email": user.email, "password": user.password, "createdAt": user.createdAt, 'updatedAt': user.updatedAt} for user in users]), 200

# Due to non crediental we user the params to get the user
# it just an example login api
@app.route("/api/users/login/<uuid:id>", methods=["POST"])
def Login(id):
  user = User.query.get(id)

  if user is None:
    return jsonify({"error": "Cannot found the user!"}), 404

  data = request.json
  username = data.get("username")
  password = data.get("password")

  if username != user.username:
    return jsonify({"error": "Invalid Username!"}), 400
  
  valid_password = bcrypt.check_password_hash(user.password, password)

  if not valid_password:
    return jsonify({"error": "Invalid Password"}), 400
  
  return jsonify({"message": "User Login Successfully!"}), 200

  
@app.route("/api/users/signin", methods=["POST"])
def SignUp():
  data = request.json
  username = data.get("username")
  name = data.get('name')
  email = data.get('email')
  password = data.get('password')

  user = User.query.filter_by(username=username).first()

  if user is not None:
    return jsonify({"error":"User Already Exists!"}), 400

  if len(username) < 3 and username == None:
    return jsonify({"error": "Invalid Username! Please provide a valid username for your account!"}), 400
  
  if len(name) < 3 and name == None:
    return jsonify({"error": "Invalid Name! Please provide a valid name for your account!"}), 400

  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' 

  if not (re.fullmatch(regex, email)):
    return jsonify({"error": "Invalid Email! Please provide a valid email address"}), 400
  
  if len(password) < 6:
    return jsonify({"error": "Password must be greater than 6 character"}), 400
  
  hash_password = bcrypt.generate_password_hash(password).decode('utf-8')

  user = User(username=username, name=name, email=email, password=hash_password)

  db.session.add(user)
  db.session.commit()

  return jsonify({"message": "User created Successfully!"}), 201
