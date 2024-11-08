#!/bin/bash

export PYTHONPATH=/usr/local/lib/python3.10/site-packages:$PYTHONPATH

echo "MySQL is up and running. Starting Django..."

# Apply database migrations
python manage.py makemigrations
echo "makemigration ran"
python manage.py migrate
echo "migrate ran"

# Start the Django application
python manage.py runserver 0.0.0.0:8000
# gunicorn -c gunicorn.py MechSimVault.wsgi
# gunicorn --log-level=info --bind 0.0.0.0:8000 MechSimVault.wsgi
