"""
Инициализирует приложение Flask
Регистрирует blueprintы
"""

from flask import Flask
from flask_pymongo import PyMongo

from .config import  Config

from dotenv import load_dotenv

from .routes.users import users_bp
from .routes.groups import groups_bp
from .routes.tasks import tasks_bp
from .routes.notification import notifications_bp
from .routes.memberships import memberships_bp
from .routes.reports import reports_bp

from .services.setup_db import setup_db

load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

app.config['MONGO'] = mongo

app.register_blueprint(users_bp, url_prefix="/api/users")
app.register_blueprint(groups_bp, url_prefix="/api/groups")
app.register_blueprint(tasks_bp, url_prefix="/api/tasks")
app.register_blueprint(notifications_bp, url_prefix="/api/notifications")
app.register_blueprint(memberships_bp, url_prefix="/api/memberships")
app.register_blueprint(reports_bp)

#Тестовый запрос, понять подключилась ли база данных
@app.route("/test/db")
def test_db():
    try:
        # Пробуем получить список коллекций (или любую простую операцию)
        collections = mongo.db.list_collection_names()
        return f'Успешное подключение к БД. Коллекции: {collections}'
    except Exception as e:
        return f'Ошибка подключения: {e}'


if __name__ == "__main__":
    with app.app_context():
        setup_db(mongo)
    app.run(debug=True)