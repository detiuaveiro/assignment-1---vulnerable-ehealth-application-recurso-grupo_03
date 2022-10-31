FROM python:3.10-alpine

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV FLASK_RUN_HOST=0.0.0.0
ENV MYSQL_HOST=db
ENV MYSQL_PORT=3306
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY .  .
CMD flask run
