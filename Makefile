.PHONY: init-dev test

init:
	sudo apt-get update
	sudo apt-get install build-essential python-dev
	pip install -r requirements.txt

init-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	nose2 -C --coverage settings

test-cov:
	nose2 -C --coverage settings --coverage-report html


