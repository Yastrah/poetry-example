install:
	pip install poetry && \
	poetry install

start:
	poetry run python bot/__main__.py