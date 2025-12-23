class Membership:
    def __init__(self, user_id, group_id, role="member"):
        self.user_id = user_id
        self.group_id = group_id
        self.role = role

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "group_id": self.group_id,
            "role": self.role
        }
