from task_manager.utils.datetime_utils import get_current_datetime
"""
Определяем класс User с атрибутами
"""

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = get_current_datetime()

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at
        }
