from flask import Blueprint, request, jsonify, current_app

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/", methods=["GET"])
def get_tasks():
    mongo = current_app.config['MONGO']
    db = mongo.db
    tasks = list(db.tasks.find({}, {"_id": 0}))
    return jsonify(tasks)

@tasks_bp.route("/", methods=["POST"])
def create_task():
    mongo = current_app.config['MONGO']
    db = mongo.db
    data = request.json
    task = {
        "title": data["title"],
        "description": data.get("description", ""),
        "priority": data.get("priority", "medium"),
        "status": data.get("status", "created"),
        "assigned_to": data.get("assigned_to", []),
        "deadline": data.get("deadline", None),
        "group_id": data.get("group_id")
    }
    result = db.tasks.insert_one(task)
    task["_id"] = str(result.inserted_id)
    return jsonify(task), 201
