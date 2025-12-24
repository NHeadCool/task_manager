from task_manager.utils.datetime_utils import get_current_datetime
"""
Определяем класс Notification с атрибутами, пока задает структуру
"""

class Notification:
    def __init__(self, user_id, task_id, type, message, is_sent=False, created_at=None):
        self.user_id = user_id
        self.task_id = task_id
        self.type = type
        self.message = message
        self.is_sent = is_sent
        self.created_at = created_at or get_current_datetime()

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "task_id": self.task_id,
            "type": self.type,
            "message": self.message,
            "is_sent": self.is_sent,
            "created_at": self.created_at
        }
