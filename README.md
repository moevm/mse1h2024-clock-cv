# mse1h2024-clock-cv

## Руководство по запуску:

Для запуска требуется [Docker](https://www.docker.com/products/docker-desktop/)


1. Переместиться в директорию `deploy`
2. `docker-compose -f docker-compose.dev.yml build --no-cache` - создание контейнеров
3. `docker-compose -f docker-compose.dev.yml up --force-recreate` --remove-orphans - запуск контейнеров

Примечание: Прописать свой ip в main.js с портом 8000
