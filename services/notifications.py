from flask import current_app
from telegram_service import send_telegram_message
"""
Сервис по отправлке уведомлений. Пока Только в telegram. 
"""

def process_notification(notification):
    success = send_telegram_message(
        chat_id=notification["chat_id"],
        text=notification["message"]
    )

    if success:
        mongo = current_app.config['MONGO']
        mongo.db.notifications.update_one(
            {"_id": notification["_id"]},
            {"$set": {"is_sent": True}}
        )
