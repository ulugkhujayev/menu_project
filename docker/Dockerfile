FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "menu_project.wsgi:application"]
