set -o errexit

pip install -r requirements.txt
yes | python manage.py collectstatic

python manage.py makemigrations
python manage.py migrate
