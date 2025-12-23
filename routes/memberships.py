from flask import Blueprint, request, jsonify, current_app
from task_manager.utils.datetime_utils import get_current_datetime
from bson import ObjectId

memberships_bp = Blueprint("memberships", __name__)

@memberships_bp.route("/", methods=["GET"])
def get_memberships():
    mongo = current_app.config['MONGO']

    memberships = list(mongo.db.group_memberships.find({}))
    for m in memberships:
        m["_id"] = str(m["_id"])
        m["user_id"] = str(m["user_id"])
        m["group_id"] = str(m["group_id"])
    return jsonify(memberships)

@memberships_bp.route("/", methods=["POST"])
def add_membership():
    mongo = current_app.config['MONGO']

    data = request.json
    membership = {
        "user_id": ObjectId(data["user_id"]),
        "group_id": ObjectId(data["group_id"]),
        "role": data.get("role", "member"),
        "joined_at": get_current_datetime()
    }
    result = mongo.db.group_memberships.insert_one(membership)
    membership["_id"] = str(result.inserted_id)
    membership["user_id"] = str(membership["user_id"])
    membership["group_id"] = str(membership["group_id"])
    return jsonify(membership), 201
