### Fake Google Forms
Проект представляет собой веб-сервис, позволяющий создавать опросники с пользовательскими вопросами. Результаты прохождения опросов отправляются в чат в Telegram. Верификация пользователей осуществляется посредством проверочного кода, отправляемого в Telegram бот.

#### Технологии Backend:
1. Django
2. Celery
3. Redis
4. TelegramAPI 

#### Технологии Frontend:
1. Bootstrap
2. HTML + CSS 
3. Jinja2  

#### Деплой:
1. docker-compose
2. nginx
3. gunicorn

## Установка и запуск сервиса
Склонируйте репозиторий из GitHub:  
```bash
git clone https://github.com/qyber1/fakegoogleforms.git
```
Заполните файл .env в корне проекта необходимыми данными.  

DJANGO_DEBUG= режим отладки (True/Falase)  
DJANGO_SECRET_KEY= секретный ключ django  

REDIS_HOST= ip адрес redis  
REDIS_PORT= порт redis  

POSTGRES_HOST= ip адрес postgres  
POSTGRES_PORT= порт postgres  
POSTGRES_NAME= имя базы данных  
POSTGRES_USER= пользователь БД  
POSTGRES_PASSWORD=пароль от БД  

BOT_TOKEN - токен телеграм бота  
BOT_CHAT_ID - это параметр chat_id, его можно узнать [здесь](https://t.me/getmyid_bot)   

Запустите Docker Compose:  
```bash
docker-compose up -d
```

Зайдите в контейнер для выполнения миграций:  
```bash
docker exec -it web sh
```
Внутри контейнера выполните следующие команды:  
```bash
python manage.py migrate
python manage.py createsuperuser
```
Перейдите в браузере по следующим ссылкам:  

Стартовая страница для регистрации и прохождения опроса: http://127.0.0.1/auth  
Админ-панель: http://127.0.0.1/admin  

Замените "127.0.0.1" на ваш IP-адрес, если развернуто на сервере.  