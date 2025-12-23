from flask import Blueprint, request, jsonify, current_app
from task_manager.utils.datetime_utils import get_current_datetime
from bson import ObjectId

notifications_bp = Blueprint("notifications", __name__)

@notifications_bp.route("/", methods=["GET"])
def get_notifications():
    mongo = current_app.config['MONGO']

    notifications = list(mongo.db.notifications.find({}))
    for n in notifications:
        n["_id"] = str(n["_id"])
        n["user_id"] = str(n["user_id"])
        n["task_id"] = str(n["task_id"])
    return jsonify(notifications)

@notifications_bp.route("/", methods=["POST"])
def create_notification():
    mongo = current_app.config['MONGO']

    data = request.json
    notification = {
        "user_id": ObjectId(data["user_id"]),
        "task_id": ObjectId(data["task_id"]),
        "type": data.get("type", "info"),
        "message": data.get("message", ""),
        "is_sent": False,
        "created_at": get_current_datetime()
    }
    result = mongo.db.notifications.insert_one(notification)
    notification["_id"] = str(result.inserted_id)
    notification["user_id"] = str(notification["user_id"])
    notification["task_id"] = str(notification["task_id"])
    return jsonify(notification), 201
