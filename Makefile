.PHONY: init-dev test lint

init:
	sudo apt-get update
	sudo apt-get install build-essential python-dev
	pip install -r requirements.txt

init-dev:
	pip install -r requirements-dev.txt

test:
	nose2 -C

test-cov:
	nose2 -C --coverage-report html

lint:
	pylint settings/ outputs/ sensors/ tests/
