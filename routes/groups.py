from flask import Blueprint, request, jsonify, current_app

groups_bp = Blueprint("groups", __name__)

@groups_bp.route("/", methods=["GET"])
def get_groups():
    mongo = current_app.config['MONGO']
    db = mongo.db
    groups = list(db.groups.find({}, {"_id": 0}))
    return jsonify(groups)

@groups_bp.route("/", methods=["POST"])
def create_group():
    mongo = current_app.config['MONGO']
    db = mongo.db
    data = request.json
    group = {
        "name": data["name"],
        "description": data.get("description", ""),
        "created_by": data.get("created_by", "unknown")
    }
    result = db.groups.insert_one(group)
    group["_id"] = str(result.inserted_id)
    return jsonify(group), 201
