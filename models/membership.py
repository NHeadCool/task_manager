from task_manager.utils.datetime_utils import get_current_datetime


class Membership:
    def __init__(self, user_id, group_id, role="member"):
        self.user_id = user_id
        self.group_id = group_id
        self.role = role
        self.joined_at = get_current_datetime()

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "group_id": self.group_id,
            "role": self.role,
            "joined_at": self.joined_at
        }
