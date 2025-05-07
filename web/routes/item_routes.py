from flask import jsonify, request
from web import app, db
from web.model.Item import Item

@app.route("/api/users", methods=["GET"])
def allItems():
  items = Item.query.all()
  if items is None:
    return jsonify({"error": "Cannot find any items."}), 404
  return jsonify([{"id": item.id, "name": item.name, "price": item.price} for item in items]), 200

@app.route("/api/users/add", methods=["POST"])
def addItem():
  data = request.json 
  name = data.get('name')
  price = data.get('price')

  if name is None and len(name) < 3:
    return jsonify({"error": "Please provide a valid name."}), 400
  
  if price < 0:
    return jsonify({"error": "Please provide a valid price."}), 400

  item = Item(name=name, price=price)
  db.session.add(item)
  db.session.commit()
  return jsonify({"message": "Item is added Successfully", "success": True}), 201

@app.route("/api/users/<int:id>", methods=["GET"])
def singleItem(id):
  item = Item.query.get(id)

  if item is None:
    return jsonify({"error": "Cannot find the item"}), 404

  return jsonify({"id": item.id, "name": item.name, "price": item.price}), 200

@app.route("/api/users/<int:id>", methods=["PUT"])
def updateItem(id):
  data = request.json
  item = Item.query.get(id)

  if item is None:
    return jsonify({"error": "Cannot find the item"}), 404
  
  item.name = data.get("name", item.name)
  item.price = data.get("price", item.price)

  db.session.commit()
  return jsonify({"message": "Item is updated Successfully"}), 200

@app.route("/api/users/<int:id>", methods=["DELETE"])
def deleteItem(id):
  item = Item.query.get(id)
  if item is None:
    return jsonify({"error": "Cannot find the item"}), 404
  
  db.session.delete(item)
  db.session.commit()
  return jsonify({"message": "Item is deleted Successfully"}), 200