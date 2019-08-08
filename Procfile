web: gunicorn -w 3 -b 0.0.0.0:$PORT application:app
init: flask db init
migrate: flask db migrate
upgrade: flask db upgrade
