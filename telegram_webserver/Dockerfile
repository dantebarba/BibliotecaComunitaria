FROM python:2

RUN pip install --upgrade pip
RUN pip install pyopenssl
RUN pip install python-telegram-bot --upgrade

ADD app.py .

CMD [ "python", "./app.py" ]
