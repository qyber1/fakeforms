import logging
from auth_user.models import User, UserResult
from .models import Question, Answer

logger = logging.getLogger(__name__)


def save_user_result(user: User, questions: list[Question], data: dict[str, str]) -> None:
    for question in questions:
        for key in data.keys():
            if key.endswith(str(question.pk)):
                try:
                    answer = Answer.objects.get(id=data[key])
                except (ValueError, Answer.DoesNotExist):
                    logging.exception('Пришло значение с поля ручного ввода')
                    answer = data[key]
                user_result = UserResult(user=user,
                                         question=question.question,
                                         answer=answer)
                user_result.save()
    logger.info('Информация о пользователе сохранена в БД')