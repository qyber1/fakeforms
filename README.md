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
git clone https://github.com/qyber1/fakeforms.git
```
Заполните файл .env в корне проекта необходимыми данными.  

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


##  Заполнение данных в БД

1. Вкладка "Тип бизнеса" - это общее направление, например: общепит, финансовый сектор, ритейл и т.д
2. Вкладка "Категория бизнеса" - у каждого типа бизнеса есть свои категории, например: общепит - бар, кафе; ритейл - магазин, автосалон
3. Вкладка "Вопросы" - у каждой категории свой набор вопросов, таким образом формируется опросник для конкретной категории
4. Вкладка "Ответы" - у каждого вопроса есть свой набор ответов