# oneapi-cc
oneapi.cc

[![CircleCI](https://circleci.com/gh/sunwei/oneapi-cc.svg?style=svg)](https://circleci.com/gh/sunwei/oneapi-cc)

### Development

```bash
pip install -r requirements/dev.txt

source .env
flask run --with-threads

curl http://localhost:5000/api/user

```
1. Read api yml
2. Convert to Nginx conf file
3. build docker image
4. Redeploy