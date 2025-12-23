from flask import Blueprint, request, jsonify, current_app

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["GET"])
def get_users():
    mongo = current_app.config['MONGO']
    db = mongo.db
    users = list(db.users.find({}, {"_id": 0}))
    return jsonify(users)

@users_bp.route("/", methods=["POST"])
def create_user():
    mongo = current_app.config['MONGO']
    db = mongo.db
    data = request.json
    user = {
        "name": data["name"],
        "email": data["email"]
    }
    result = db.users.insert_one(user)
    user["_id"] = str(result.inserted_id)
    return jsonify(user), 201
