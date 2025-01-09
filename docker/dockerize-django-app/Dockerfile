FROM python:3.14.0a3-slim-bookworm

WORKDIR /app/food

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "dockerize.wsgi:application" ]