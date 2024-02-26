import logging
import requests

from django.conf import settings
from celery import shared_task
from auth_user.models import User, UserResult


logger = logging.getLogger(__name__)


@shared_task(bind=True)
def send_info_about_user(self, email: str) -> None:
    """Отправляет результат прохождения опроса в телеграмм"""

    logger.info('Отправка результата в ТГ')
    user = User.objects.get(email=email)
    all_answers = UserResult.objects.filter(user=user)
    result = '\n'.join([f"{answer.question} - {answer.answer}" for answer in all_answers])
    text = f"Пользователь: {user}\n" \
           f"Ниша: {user.bis_type}\n" \
           f"Категория: {user.cat}\n" \
           f"{result}"
    params = {"chat_id": settings.CHAT_ID, "text": text}
    try:
        requests.post(url=settings.BOT_URL, params=params)
        logger.info(f'Сообщение с результатом отправлено в чат {settings.CHAT_ID}')
    except requests.exceptions.RequestException:
        logger.error(f"Произошла ошибка при отправке результата в чат {settings.CHAT_ID}", exc_info=True)
