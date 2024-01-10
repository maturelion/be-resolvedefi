#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Upgrading pip and installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Applying database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

# echo "Creating superuser..."
# python manage.py createsuperuser --noinput
