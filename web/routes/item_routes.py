from flask import jsonify, request
from web import app, db
from web.model.Item import Item
import uuid

@app.route("/api/items", methods=["GET"])
def getAllItems():
  items = Item.query.all()

  if items is None:
    return jsonify({"error": "Cannot find any items"}), 400

  return jsonify([{"id": item.id, "name": item.name, "price": item.price, "createdAt": item.createdAt, "updatedAt": item.updatedAt, "owner": item.owner} for item in items]), 200


@app.route("/api/item/add/<uuid:UserId>", methods=["POST"])
def addItem(UserId):
  data = request.json
  name = data.get("name")
  price = data.get("price")

  if len(name) < 3 and name is None:
    return jsonify({"error": "Invalid Item Name! Please provide a valid name"}), 400
  
  if price < 0 and price is None:
    return jsonify({"error": "Invalid Price! Please provide a valid price"}), 400

  item = Item(name=name, price=price, owner=UserId)

  if item is None:
    return jsonify({"error": "Invalid Item Created!"}), 400

  db.session.add(item)
  db.session.commit()

  return jsonify({"message": "Item Created Successfully!"}), 201

@app.route("/api/item/update/<uuid:id>", methods=["PUT"])
def updateItem(id):
  item = Item.query.get(id)

  if item is None:
    return jsonify({"error": "Cannot find the item"}), 404

  data = request.json 
  item.name = data.get("name", item.name)
  item.price = data.get("price", item.price)

  return jsonify({"error": "Item updated Successfully!"}), 200

@app.route("/api/item/<uuid:id>", methods=["GET"])
def getSingleItem(id):
  item = Item.query.get(id)

  if item is None:
    return jsonify({"error": "Cannot find the item"}), 404
  
  return jsonify({"id": item.id, "name": item.name, "price": item.price, "createdAt": item.createdAt, "updatedAt": item.updatedAt, owner: item.owner}), 200

@app.route("/api/item/delete/<uuid:id>", methods=["DELETE"])
def removeItem(id):
  item = Item.query.get(id)

  if item is None:
    return jsonify({"error": "Cannot find the item"}), 404

  db.session.delete(item)
  db.session.commit()

  return jsonify({"message": "Item has Deleted Successfully!"}), 200