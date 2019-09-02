CUR_TOKEN = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjczOTA1MDAsIm5iZiI6MTU2NzM5MDUwMCwianRpIjoiNmRlMjA1ZWItNGQyMy00MjI0LTgwNDQtNzkzMWE1N2RmY2UxIiwiZXhwIjo4Nzk2NzM5MDUwMCwiaWRlbnRpdHkiOjEsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.ImkEhbYIJI3yYI2Nu9sZGRgmXPDAS8uREYjZW1OZbNk

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
	  '{"user": {"username":"wayde222", "password":"abcd", "email":"wayde222@gmail.com"}}' \
	  http://localhost:5000/api/users

get-user:
	curl -H 'Content-Type: application/json' -X GET \
	 -H "Authorization: Token $(CUR_TOKEN)" \
	  http://localhost:5000/api/user
	  
create-namespace:
	curl -H 'Content-Type: application/json' -X POST -d \
	  '{"namespace": {"name": "api"}}' \
	  -H "Authorization: Token $(CUR_TOKEN)" \
	  http://localhost:5000/api/namespaces

get-namespace:
	curl -H 'Content-Type: application/json' -X GET \
	  http://localhost:5000/api/namespaces/api

clean:
	rm -rf dev.db && rm -rf migrations

heroku-login:
	heroku auth:login

heroku-dev-token:
	heroku auth:token

heroku-db-upgrade:
	heroku run upgrade --app oneapi-server