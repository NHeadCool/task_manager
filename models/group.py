from task_manager.utils.datetime_utils import get_current_datetime


class Group:
    def __init__(self, name, description, created_by, created_at=None):
        self.name = name
        self.description = description
        self.created_by = created_by  # ObjectId пользователя
        self.created_at = created_at or get_current_datetime()

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "created_by": self.created_by,
            "created_at": self.created_at
        }
