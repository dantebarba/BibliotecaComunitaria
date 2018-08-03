FROM python:2-alpine

RUN pip install --upgrade pip
RUN pip install requests
RUN pip install python-telegram-bot --upgrade

ADD . .

CMD [ "python", "./app.py" ]
