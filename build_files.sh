pip install -r require.txt

python manage.py collectstatic --no-input

# python manage.py createsuperuser --no-input

# python manage.py makemigrations

# python manage.py migrate

# python -m gunicorn flairest_project.asgi:application -k uvicorn.workers.UvicornWorker - off
# python manage.py runserver - on - but need 0.0.0.0 port/s
