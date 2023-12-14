FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /coursehelper
COPY requirements.txt .
RUN pip install --upgrade pip
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
COPY . .

EXPOSE 80
CMD python manage.py runserver 0.0.0.0:80
