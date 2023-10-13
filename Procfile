release: python manage.py migrate
web: daphne incomeexpensesapi.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A incomeexpensesapi.celery worker -l info
celerybeat: celery -A incomeexpensesapi beat -l INFO 
celeryworker2: celery -A incomeexpensesapi.celery worker & celery -A incomeexpensesapi beat -l INFO & wait -n




