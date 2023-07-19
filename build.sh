#!/bin/bash
#build the project
echo "Building the projects..."
python3.9 -m pip install -r requirements.txt

# run theproject

echo "Make Migrations.."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput


echo "collect static.."
python3.9 manage.py collectstatic --noinput --clear