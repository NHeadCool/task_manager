from flask import Blueprint, request, jsonify, current_app
from task_manager.utils.datetime_utils import get_current_datetime
from bson import ObjectId

groups_bp = Blueprint("groups", __name__)

@groups_bp.route("/", methods=["GET"])
def get_groups():
    mongo = current_app.config['MONGO']

    groups = list(mongo.db.groups.find({}))
    for g in groups:
        g["_id"] = str(g["_id"])
        g["created_by"] = str(g["created_by"])
    return jsonify(groups)

@groups_bp.route("/", methods=["POST"])
def create_group():
    mongo = current_app.config['MONGO']

    data = request.json
    group = {
        "name": data["name"],
        "description": data.get("description", ""),
        "created_by": ObjectId(data["created_by"]),
        "created_at": get_current_datetime()
    }
    result = mongo.db.groups.insert_one(group)
    group["_id"] = str(result.inserted_id)
    group["created_by"] = str(group["created_by"])
    return jsonify(group), 201
