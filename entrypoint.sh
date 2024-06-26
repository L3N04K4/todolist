#!/bin/bash

# Apply Django migrations
python manage.py migrate

# Start the Django development server
if [ "$DJANGO_SERVICE" = "flower" ]
then
  celery -A todolist flower --port=5555
else
  python manage.py runserver 0.0.0.0:8000
fi