pip3 install -r api/requirements.txt

python3 api/manage.py makemigrations app
python3 api/manage.py makemigrations
python3 api/manage.py migrate
python3 api/manage.py runserver
