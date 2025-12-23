from flask import Blueprint, request, jsonify, current_app

notifications_bp = Blueprint("notifications", __name__)

@notifications_bp.route("/", methods=["GET"])
def get_notifications():
    mongo = current_app.config['MONGO']
    db = mongo.db
    notifications = list(db.notifications.find({}, {"_id": 0}))
    return jsonify(notifications)

@notifications_bp.route("/", methods=["POST"])
def create_notification():
    mongo = current_app.config['MONGO']
    db = mongo.db
    data = request.json
    notification = {
        "title": data.get("title", "No title"),
        "message": data.get("message", ""),
        "user_id": data.get("user_id"),
        "read": False
    }
    result = db.notifications.insert_one(notification)
    notification["_id"] = str(result.inserted_id)
    return jsonify(notification), 201
