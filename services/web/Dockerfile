FROM python:3.11

WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat-traditional

RUN pip install --upgrade pip
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

#chmod +x services/web/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]