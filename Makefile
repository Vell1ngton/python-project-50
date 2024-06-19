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