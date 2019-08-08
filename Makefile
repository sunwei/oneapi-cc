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

get-user:
	curl -H 'Content-Type: application/json' -X GET \
	 -H "Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjUyMzM0OTIsIm5iZiI6MTU2NTIzMzQ5MiwianRpIjoiMjliNjEwZjMtMmNlNy00NDA5LWIxOWEtZGMzOWU4MmMwZGJjIiwiZXhwIjoxNTY1MjM0MzkyLCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.oaDglDOMG6A8TvdmhGGrCc2Z2w_78BbiHqk6M4UL1kU" \
	  http://localhost:5000/api/user

clean:
	rm -rf dev.db && rm -rf migrations

heroku-login:
	heroku auth:login

heroku-dev-token:
	heroku auth:token

heroku-db-upgrade:
	heroku run upgrade --app oneapi-server