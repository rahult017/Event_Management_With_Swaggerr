#!/bin/sh
python manage.py collectstatic --noinput

gunicorn Event_Management_With_Swaggerr.wsgi:application --workers 8 \
    --bind 0.0.0.0:8000 \
    --log-file /usr/src/app/logs/gunicorn/gunicorn.log \
    --access-logfile /usr/src/app/logs/gunicorn/access.log \
    --error-logfile /usr/src/app/logs/gunicorn/error.log
