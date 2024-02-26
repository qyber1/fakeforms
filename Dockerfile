FROM python:3.11-alpine

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "form.wsgi"]