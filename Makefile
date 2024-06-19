install:
	poetry install

build:
	poetry build

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 project50

pytest:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=project50 --cov-report xml