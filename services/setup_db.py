from pymongo import MongoClient
import os

def setup_db(mongo):
    """Инициализация базы при первом запуске."""
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client['task_manager']

    # Создаем начальных пользователей
    if db.users.count_documents({}) == 0:
        users = [
            {"name": "Nikita", "email": "nikita@example.com"},
            {"name": "Kolia", "email": "kolia@example.com"},
            {"name": "Gleb", "email": "gleb@example.com"}
        ]
        db.users.insert_many(users)
        print("Users initialized")

    # Создаем начальные группы
    if db.groups.count_documents({}) == 0:
        groups = [
            {"name": "UCD Module", "description": "Группа модульного задания по UCD", "created_by": "Nikita"},
            {"name": "Architecture Module", "description": "Группа модульного задания по Архитектуре", "created_by": "Gleb"}
        ]
        db.groups.insert_many(groups)
        print("Groups initialized")

    # Создаем начальные задачи
    if db.tasks.count_documents({}) == 0:
        tasks = [
            {
                "group_id": str(db.groups.find_one({"name": "UCD Module"})["_id"]),
                "title": "Сделать Job Stories",
                "description": "Составить Job stories для проекта",
                "priority": "high",
                "status": "created",
                "assigned_to": [],
                "deadline": None
            }
        ]
        db.tasks.insert_many(tasks)
        print("Tasks initialized")
