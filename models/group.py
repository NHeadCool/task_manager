class Group:
    def __init__(self, name, description, created_by):
        self.name = name
        self.description = description
        self.created_by = created_by

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "created_by": self.created_by
        }