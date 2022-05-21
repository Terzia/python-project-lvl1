# Makefile

install: #Создание виртуального окружения
	poetry install


brain-games: #Запустить проект
	poetry run brain-games


build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl


make lint:
	poetry run flake8 brain_games
