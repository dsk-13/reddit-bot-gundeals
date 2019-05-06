FROM python:3-alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
CMD python /app/bot/bot.py
