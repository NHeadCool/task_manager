from task_manager.utils.datetime_utils import get_current_datetime
"""
Сервис нужен чтобы создать бд при первом запуске. setup_db В том числе проверяет
есть таблицы или нет, заполнены или нет и заполняет. Нужно чтобы были первые данные
удобно для отладки
"""
def setup_db(mongo):
    db = mongo.db

    if db.users.count_documents({}) == 0:
        users = [
            {"name": "Nikita", "email": "nikita@example.com", "created_at": get_current_datetime()},
            {"name": "Kolia", "email": "kolia@example.com", "created_at": get_current_datetime()},
            {"name": "Gleb", "email": "gleb@example.com", "created_at": get_current_datetime()}
        ]
        db.users.insert_many(users)
        print("Users initialized")

    if db.groups.count_documents({}) == 0:
        nikita_id = db.users.find_one({"name": "Nikita"})["_id"]
        gleb_id = db.users.find_one({"name": "Gleb"})["_id"]

        groups = [
            {"name": "UCD Module", "description": "Group of UCD Module",
             "created_by": nikita_id, "created_at": get_current_datetime()},
            {"name": "Architecture Module", "description": "Group of Architecture Module",
             "created_by": gleb_id, "created_at": get_current_datetime()}
        ]
        db.groups.insert_many(groups)
        print("Groups initialized")

    if db.group_memberships.count_documents({}) == 0:
        ucd_group_id = db.groups.find_one({"name": "UCD Module"})["_id"]
        arch_group_id = db.groups.find_one({"name": "Architecture Module"})["_id"]
        users = list(db.users.find({}))
        memberships = [
            {"user_id": users[0]["_id"], "group_id": ucd_group_id, "role": "admin", "joined_at": get_current_datetime()},
            {"user_id": users[1]["_id"], "group_id": ucd_group_id, "role": "member", "joined_at": get_current_datetime()},
            {"user_id": users[2]["_id"], "group_id": arch_group_id, "role": "admin", "joined_at": get_current_datetime()},
        ]
        db.group_memberships.insert_many(memberships)
        print("Group memberships initialized")

    if db.tasks.count_documents({}) == 0:
        ucd_group_id = db.groups.find_one({"name": "UCD Module"})["_id"]
        nikita_id = db.users.find_one({"name": "Nikita"})["_id"]
        tasks = [
            {
                "group_id": ucd_group_id,
                "title": "Do Job Stories",
                "description": "Do Job stories for project",
                "priority": "high",
                "status": "created",
                "deadline": None,
                "created_by": nikita_id,
                "assigned_to": [],
                "created_at": get_current_datetime()
            }
        ]
        db.tasks.insert_many(tasks)
        print("Tasks initialized")

    if db.notifications.count_documents({}) == 0:
        print("Notifications collection ready")
