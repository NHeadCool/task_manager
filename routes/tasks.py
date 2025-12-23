from flask import Blueprint, request, jsonify, current_app
from task_manager.utils.datetime_utils import get_current_datetime
from bson import ObjectId

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/", methods=["GET"])
def get_tasks():
    mongo = current_app.config['MONGO']

    tasks = list(mongo.db.tasks.find({}))
    for t in tasks:
        t["_id"] = str(t["_id"])
        t["group_id"] = str(t["group_id"])
        t["created_by"] = str(t.get("created_by"))
        t["assigned_to"] = [str(uid) for uid in t.get("assigned_to", [])]
    return jsonify(tasks)

@tasks_bp.route("/", methods=["POST"])
def create_task():
    mongo = current_app.config['MONGO']

    data = request.json
    task = {
        "group_id": ObjectId(data["group_id"]),
        "title": data["title"],
        "description": data.get("description", ""),
        "priority": data.get("priority", "medium"),
        "status": "created",
        "deadline": data.get("deadline"),  # ожидаем ISO строку или None
        "created_by": ObjectId(data["created_by"]),
        "assigned_to": [ObjectId(uid) for uid in data.get("assigned_to", [])],
        "created_at": get_current_datetime()
    }
    result = mongo.db.tasks.insert_one(task)
    task["_id"] = str(result.inserted_id)
    task["group_id"] = str(task["group_id"])
    task["created_by"] = str(task["created_by"])
    task["assigned_to"] = [str(uid) for uid in task["assigned_to"]]
    return jsonify(task), 201
