#!/bin/sh

export SECURE_KEY=$(uuidgen|base64)
python manage.py makemigrations && python manage.py migrate
python manage.py collectstatic --noinput
gunicorn portfolio.wsgi:application -b :8000