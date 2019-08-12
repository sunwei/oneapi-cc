CUR_DIR = $(CURDIR)

mac-install:
	brew install postgresql
	export LDFLAGS="-L/usr/local/opt/openssl/lib"
	pip3 install -r requirements/dev.txt

install:
	pip3 install -r requirements/dev.txt

run:
	flask run --with-threads

db:
	flask db init && flask db migrate && flask db upgrade

register:
	curl -H 'Content-Type: application/json' -X POST -d \
	  '{"user": {"username":"wayde111", "password":"abcd", "email":"wayde111@gmail.com"}}' \
	  http://localhost:5000/api/users

get-user:
	curl -H 'Content-Type: application/json' -X GET \
	 -H "Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjUzMzU0NzUsIm5iZiI6MTU2NTMzNTQ3NSwianRpIjoiMjk2YmJhMTgtMTVhZC00MzJkLWJjNWEtMmJlYzQ3ZGNjYmIwIiwiZXhwIjo4Nzk2NTMzNTQ3NSwiaWRlbnRpdHkiOjEsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.QVGpxdh6lVssRor1PJ-besyLMKgFnN9WuFoF-53pmqs" \
	  http://localhost:5000/api/user

clean:
	rm -rf dev.db && rm -rf migrations

heroku-login:
	heroku auth:login

heroku-dev-token:
	heroku auth:token

heroku-db-upgrade:
	heroku run upgrade --app oneapi-server