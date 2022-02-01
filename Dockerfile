FROM python:3.5-buster

ADD . .

ENV FLASK_APP=app.py

RUN pip install -r requirements.txt

EXPOSE 7777

CMD flask run --port 7777 --host 0.0.0.0
