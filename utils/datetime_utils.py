"""
Функция определяет моментальное время из внешнего API (Sber).
Нужно, чтобы приписать к данным created_at
"""
import os

import requests
from datetime import datetime

def get_current_datetime():
    URL = os.getenv("CURRENT_TIME_API_SERVICE_URI")

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        current_time = response.json().get("formatted")
        if current_time:
            return current_time
    except Exception:
        pass

    return datetime.utcnow().isoformat()