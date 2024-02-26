import logging
from requests import post
from random import randint
from celery import shared_task
from .cache import set_user_code
from django.conf import settings

logger = logging.getLogger(__name__)


@shared_task(bind=True)
def send_secret_code_on_email(self, email: str) -> None:
    logger.info('Задача на генерацию и отправка кода')
    code = randint(1000, 9999)
    set_user_code(email, code)
    params = {"chat_id": settings.CHAT_ID, "text": code}
    post(url=settings.BOT_URL,
         params=params)
    return code
