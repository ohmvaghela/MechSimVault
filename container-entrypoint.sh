#!/bin/sh


#######################################
## Use this only with docker compose ##
#######################################
# check_mysql() {
#   mysqladmin ping -h mysql -u root -ppassword > /dev/null 2>&1
# }

# until check_mysql; do
#   echo "Waiting for MySQL..."
#   sleep 2
# done

#######################################

echo "MySQL is up and running. Starting Django..."

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Start the Django application
python manage.py runserver 0.0.0.0:8000
