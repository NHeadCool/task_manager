from flask import Blueprint, request, jsonify, current_app

memberships_bp = Blueprint("memberships", __name__, url_prefix="/api/memberships")

@memberships_bp.route("/", methods=["POST"])
def add_member():
    data = request.json
    membership = {
        "user_id": data["user_id"],
        "group_id": data["group_id"],
        "role": data.get("role", "member")
    }
    result = current_app.mongo.db.memberships.insert_one(membership)
    membership["_id"] = str(result.inserted_id)
    return jsonify(membership), 201

@memberships_bp.route("/<group_id>", methods=["GET"])
def get_group_members(group_id):
    members = list(current_app.mongo.db.memberships.find({"group_id": group_id}))
    for m in members:
        m["_id"] = str(m["_id"])
    return jsonify(members)
