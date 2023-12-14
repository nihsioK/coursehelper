FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /coursehelper
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8080
CMD python manage.py runserver 0.0.0.0:8080
