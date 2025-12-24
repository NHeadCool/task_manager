from task_manager.utils.datetime_utils import get_current_datetime
"""
Определяем класс Task с атрибутами
"""

class Task:
    def __init__(self, group_id, title, description, priority, status="created", deadline=None, created_by=None, assigned_to=None, created_at=None):
        self.group_id = group_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.deadline = deadline
        self.created_by = created_by
        self.assigned_to = assigned_to or []
        self.created_at = created_at or get_current_datetime()

    def to_dict(self):
        return {
            "group_id": self.group_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "deadline": self.deadline,
            "created_by": self.created_by,
            "assigned_to": self.assigned_to,
            "created_at": self.created_at
        }
