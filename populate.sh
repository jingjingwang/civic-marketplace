#!/bin/sh

python manage.py makemigrations dashboard
python manage.py makemigrations account
python manage.py migrate
python manage.py loaddata skills
python manage.py loaddata causes
# python manage.py loaddata testdata
