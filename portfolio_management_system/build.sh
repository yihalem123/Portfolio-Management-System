set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --yes


python manage.py makemigrations
python manage.py migrate
