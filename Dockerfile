FROM python:2-jessie
COPY . /app
RUN pip install -r /app/requirements.txt
CMD python /app/bot/bot.py
