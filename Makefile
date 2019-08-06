CUR_DIR = $(CURDIR)

install:
	pip3 install -r requirements/dev.txt

run:
	flask run --with-threads
