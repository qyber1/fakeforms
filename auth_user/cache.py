from typing import Any

from django.conf import settings
import redis


class RedisStorage:
    """
    Класс, представляющий хранилище данных в Redis.

    Attributes:
        connector (redis.Redis): Экземпляр подключения к Redis, использующий параметры из настроек Django.

    Methods:
        set_user_code - устанавливает код пользователя в Redis.

        get_user_code - получает код пользователя из Redis.

    """
    connector = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,
                            db=1, decode_responses=True)

    @classmethod
    def set_user_code(cls, email: str, code: int) -> None:
        cls.connector.set(email, code)

    @classmethod
    def get_user_code(cls, email: str) -> str:
        result = cls.connector.get(email)
        return result


def set_user_code(email: str, code: int) -> Any:
    return RedisStorage.set_user_code(email, code)


def get_user_code(email: str) -> str:
    return RedisStorage.get_user_code(email)
