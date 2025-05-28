"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import pytest
import os

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


@pytest.mark.parametrize("status", ["success", "expired", "failed"])
def test_log_event(status):
    username = "test"

    # Очистити лог файл і хендлери лише при першому виклику
    if status == "success":
        if os.path.exists("login_system.log"):
            os.remove("login_system.log")

    # При кожному виклику скидаємо хендлери, щоб basicConfig спрацював
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Викликаємо функцію логування
    log_event(username, status)

    # Після трьох викликів (тобто у останньому тесті) читаємо і перевіряємо весь файл
    if status == "failed":
        with open("login_system.log", "r") as f:
            log_content = f.read()

        for s in ["success", "expired", "failed"]:
            assert f"Username: {username}, Status: {s}" in log_content