#!/bin/sh

# Function to check if MySQL is running
check_mysql() {
  mysqladmin ping -h mysql -u root -ppassword > /dev/null 2>&1
}

# Wait for MySQL to be available
until check_mysql; do
  echo "Waiting for MySQL..."
  sleep 2
done

echo "MySQL is up and running. Starting Django..."

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Start the Django application
python manage.py runserver 0.0.0.0:8000
