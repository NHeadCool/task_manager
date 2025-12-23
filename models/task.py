from datetime import datetime

class Task:
    def __init__(self, group_id, title, description, priority="medium", status="created", assigned_to=None, deadline=None):
        self.group_id = group_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.assigned_to = assigned_to or []
        self.deadline = deadline
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            "group_id": self.group_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "deadline": self.deadline,
            "created_at": self.created_at.isoformat()
        }
