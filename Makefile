CUR_DIR = $(CURDIR)

install:
	pip3 install -r requirements/dev.txt

run:
	flask run --with-threads

db:
	flask db init && flask db migrate && flask db upgrade

register:
	curl -H 'Content-Type: application/json' -X POST -d \
	  '{"user": {"username":"wayde", "password":"abcd", "email":"wayde@gmail.com"}}' \
	  http://localhost:5000/api/users

clean:
	rm -rf dev.db && rm -rf migrations

heroku-login:
	heroku auth:login

heroku-dev-token:
	heroku auth:token

heroku-db-upgrade:
	heroku run upgrade --app oneapi-server