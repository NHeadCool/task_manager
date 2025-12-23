from flask import Blueprint, render_template, current_app
from datetime import datetime

reports_bp = Blueprint("reports", __name__, url_prefix="/report")

def format_datetime_safe(dt):
    if dt:
        return dt.strftime("%Y-%m-%d %H:%M:%S") if hasattr(dt, 'strftime') else str(dt)
    return "—"

@reports_bp.route("/users")
def users_report():
    mongo = current_app.config['MONGO']
    users = list(mongo.db.users.find({}, {"_id": 0, "name": 1, "email": 1, "created_at": 1}))
    for u in users:
        u['created_at'] = format_datetime_safe(u.get('created_at'))
    return render_template("users_report.html", users=users)

@reports_bp.route("/groups")
def groups_report():
    mongo = current_app.config['MONGO']
    groups = list(mongo.db.groups.find({}, {"_id": 0, "name": 1, "description": 1, "created_by": 1, "created_at": 1}))
    for g in groups:
        g['created_at'] = format_datetime_safe(g.get('created_at'))
    return render_template("groups_report.html", groups=groups)

@reports_bp.route("/tasks")
def tasks_report():
    mongo = current_app.config['MONGO']
    tasks = list(mongo.db.tasks.find({}, {"_id": 0, "title": 1, "description": 1, "priority": 1,
                                          "status": 1, "deadline": 1, "created_by": 1, "assigned_to": 1, "created_at": 1}))
    for t in tasks:
        t['created_at'] = format_datetime_safe(t.get('created_at'))
        t['deadline'] = format_datetime_safe(t.get('deadline'))
    return render_template("tasks_report.html", tasks=tasks)

@reports_bp.route("/notifications")
def notifications_report():
    mongo = current_app.config['MONGO']
    notifications = list(mongo.db.notifications.find({}, {"_id": 0, "user_id": 1, "task_id": 1,
                                                          "type": 1, "message": 1, "is_sent": 1, "created_at": 1}))
    for n in notifications:
        n['created_at'] = format_datetime_safe(n.get('created_at'))
    return render_template("notifications_report.html", notifications=notifications)
