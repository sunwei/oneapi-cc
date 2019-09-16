CUR_TOKEN = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg2MTIzMzQsIm5iZiI6MTU2ODYxMjMzNCwianRpIjoiMDAxZGJmYjUtYzBkYS00YjYxLTg2NGItNmVkNWQ3Zjg0Mjk0IiwiZXhwIjo4Nzk2ODYxMjMzNCwiaWRlbnRpdHkiOjEsImZyZXNoIjp0cnVlLCJ0eXBlIjoiYWNjZXNzIn0.2ahUoErjGGaD3BVHnrRVvhQQSVyiJBKGNtIloC6YI7U

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

login:
	curl -H 'Content-Type: application/json' -X POST -d \
	  '{"user": {"password":"abcd", "email":"wayde222@gmail.com"}}' \
       http://localhost:5000/api/users/login

create-namespace:
	curl -H 'Content-Type: application/json' -X POST -d \
	  '{"namespace": {"name": "api"}}' \
	  -H "Authorization: Token $(CUR_TOKEN)" \
	  http://localhost:5000/api/namespaces

get-namespace:
	curl -H 'Content-Type: application/json' -X GET \
	  http://localhost:5000/api/namespaces/api

create-api:
	curl -H 'Content-Type: application/json' -X POST -d \
	  '{"api": {"body": "ewogICJ2ZXJzaW9uIjogInYxIiwKICAibmFtZXNwYWNlIjogIndhcmVob3VzZSIsCiAgIm1ldGFkYXRhIjogewogICAgImF1dGhvciI6ICJTdW4gV2VpIiwKICAgICJlbWFpbCI6ICJ3YXlkZS5zdW5AZ21haWwuY29tIiwKICAgICJyZXBvc2l0b3J5IjogImh0dHBzOi8vZ2l0aHViLmNvbS9zdW53ZWkvZmxhc2stc2FtbDItb2t0YSIsCiAgICAiZGVzY3JpcHRpb24iOiAidXNlZCBmb3Igd2hhdC4uLiIKICB9LAogICJhcGlzIjogWwogICAgewogICAgICAibmFtZSI6ICJXYXJlaG91c2UgSW52ZW50b3J5IiwKICAgICAgInNwZWNzIjogImh0dHBzOi8vZXhhbXBsZS5jb20vc3dhZ2dlci5qc29uIiwKICAgICAgInBhdGgiOiAiL3dhcmVob3VzZS9pbnZlbnRvcnkiLAogICAgICAiZGVzY3JpcHRpb24iOiAidXNlZCBmb3Igd2hhdC4uLiIsCiAgICAgICJhbm5vdGF0aW9ucyI6ICJsYWJlbHMgb3IgdGFncy4uLiIKICAgIH0sCiAgICB7CiAgICAgICJuYW1lIjogIldhcmVob3VzZSBQcmljaW5nIiwKICAgICAgInNwZWNzIjogImh0dHBzOi8vZXhhbXBsZS5jb20vc3dhZ2dlci5qc29uIiwKICAgICAgInBhdGgiOiAiL3dhcmVob3VzZS9wcmljaW5nIiwKICAgICAgImRlc2NyaXB0aW9uIjogInVzZWQgZm9yIHdoYXQuLi4iLAogICAgICAiYW5ub3RhdGlvbnMiOiAibGFiZWxzIG9yIHRhZ3MuLi4iCiAgICB9CiAgXSwKICAidXBzdHJlYW1zIjogWwogICAgewogICAgICAibmFtZSI6ICJJbnZlbnRvcnkiLAogICAgICAiZW5kcG9pbnRzIjogWwogICAgICAgICJhcGkxLmNvbSIsCiAgICAgICAgImFwaTIuY29tIiwKICAgICAgICAiYXBpMy5jb20iCiAgICAgIF0KICAgIH0sCiAgICB7CiAgICAgICJuYW1lIjogIlByaWNpbmciLAogICAgICAiZW5kcG9pbnRzIjogWwogICAgICAgICJhcGkzLmNvbSIsCiAgICAgICAgImFwaTQuY29tIiwKICAgICAgICAiYXBpNS5jb20iCiAgICAgIF0KICAgIH0KICBdLAogICJyb3V0ZVNwZWNpZmljYXRpb25zIjogWwogICAgewogICAgICAiYXBpUmVmIjogIldhcmVob3VzZSBJbnZlbnRvcnkiLAogICAgICAidXBzdHJlYW1SZWYiOiAiSW52ZW50b3J5IiwKICAgICAgInBvbGljaWVzIjp7CiAgICAgICAgImF1dGhlbnRpY2F0aW9uIjogewogICAgICAgICAgInR5cGUiOiAiQmFzaWMiCiAgICAgICAgfQogICAgICB9CiAgICB9LCB7CiAgICAgICJhcGlSZWYiOiAiV2FyZWhvdXNlIFByaWNpbmciLAogICAgICAidXBzdHJlYW1SZWYiOiAiUHJpY2luZyIsCiAgICAgICJwb2xpY2llcyI6ewogICAgICAgICJhdXRoZW50aWNhdGlvbiI6IHsKICAgICAgICAgICJ0eXBlIjogIkJhc2ljIgogICAgICAgIH0KICAgICAgfQogICAgfQogIF0KfQ=="}}' \
	  -H "Authorization: Token $(CUR_TOKEN)" \
	  http://localhost:5000/api/apigws

clean:
	rm -rf dev.db && rm -rf migrations

heroku-login:
	heroku auth:login

heroku-dev-token:
	heroku auth:token

heroku-db-upgrade:
	heroku run upgrade --app oneapi-server