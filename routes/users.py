"""
Маршруты для users. Опр запросы Get (получить весь список пользователей)
и POST (чтобы создать пользователя)
"""
from flask import Blueprint, request, jsonify, current_app, current_app
from task_manager.utils.datetime_utils import get_current_datetime

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["GET"])
def get_users():
    mongo = current_app.config['MONGO']

    users = list(mongo.db.users.find({}, {"_id": 1, "name": 1, "email": 1, "created_at": 1}))
    for u in users:
        u["_id"] = str(u["_id"])
    return jsonify(users)

@users_bp.route("/", methods=["POST"])
def create_user():
    mongo = current_app.config['MONGO']
    data = request.json
    user = {
        "name": data["name"],
        "email": data["email"],
        "created_at": get_current_datetime()
    }
    result = mongo.db.users.insert_one(user)
    user["_id"] = str(result.inserted_id)
    return jsonify(user), 201

