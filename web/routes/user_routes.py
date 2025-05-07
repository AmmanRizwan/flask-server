from flask import jsonify, request
from web import app, db
from web.model.User import User

@app.route("/api/users", methods=["GET"])
def getAllUser():
  users = User.query.all()

  if users is None:
    return jsonify({"error": "Cannot find the user"}), 404

  return jsonify([{"id": user.id, "username": user.username, "name": user.name, "email": user.email, "password": user.password} for user in users]), 200

@app.route("/api/users", methods=["POST"])
def addUser():
  data = request.json
  username = data.get("username")
  name = data.get("name")
  email = data.get("email")
  password = data.get("password")

  if len(username) < 3 and username is None:
    return jsonify({"error": "Please provide a valid username"}), 400
  
  if len(name) < 3 and name is None:
    return jsonify({"error": "Please provide a valid name"}), 400

  if len(password) < 6:
    return jsonify({"error": "Password must be greater than 6 characters."}), 400

  user = User(username=username, name=name, email=email, password=password)
  db.session.add(user)
  db.session.commit()
  return jsonify({"message": "User is added Successfully!"}), 201
