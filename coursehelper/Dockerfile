FROM python:3.9-alpine
ENV PYTHONBUFFERED 1

WORKDIR /coursehelper
COPY requirements.txt .
RUN pip install --upgrade pip
# RUN apt-get update && apt-get install -y libpq-dev
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:80


