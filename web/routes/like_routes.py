from flask import request, jsonify
from web import db, app 
from web.model.Like import Like

@app.route("/api/like/all", methods=["GET"])
def allLike():
  likes = Like.query.all() 
  if likes is None:
    return jsonify({"error": "cannot find the like!"}), 404

  return jsonify([{"id": like.id, "like": like.like} for like in likes]), 200