.PHONY: default venv lint pretty dev-start dev-build prod-rsync prod-stop prod-build prod-migrate prod-stop
# Тест
default:
	@echo "There is no default target."
# Создание окружения
venv:
	remove -rf venv
	python -m venv venv
	./venv/bin/pip install -r requirements.txt
# Проверка качества кода (mac, linux)
lint:
	./venv/bin/black --check -l 79 clockcv
	./venv/bin/flake8 clockcv
	./venv/bin/isort -c --src clockcv --profile black -l 79 clockcv
# Проверка красоты кода (mac, linux)
pretty:
	./venv/bin/black -l 79 clockcv
	./venv/bin/flake8 clockcv
	./venv/bin/isort --src clockcv --profile black -l 79 clockcv
# Проверка качества кода (windows)
lint-win:
	./venv/Scripts/black --check -l 79 clockcv
	./venv/Scripts/flake8 clockcv
	./venv/Scripts/isort -c --src clockcv --profile black -l 79 clockcv
# Проверка красоты кода (windows)
pretty-win:
	./venv/Scripts/black -l 79 clockcv
	./venv/Scripts/flake8 clockcv
	./venv/Scripts/isort --src clockcv --profile black -l 79 clockcv
# Запуск Доккер контейнеров
dev-start:
	docker-compose -f deployments/docker-compose.dev.yml up --force-recreate --remove-orphans
# Остановка Доккер контейнеров
dev-stop:
	docker-compose -f deployments/docker-compose.dev.yml down
# Сборка
dev-build:
	docker-compose -f deployments/docker-compose.dev.yml build --no-cache