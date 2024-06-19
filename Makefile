install:
	poetry install

build:
	poetry build

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check:
	poetry run flake8 gendiff
	poetry run pytest --cov=gendiff