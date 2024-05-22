# mse1h2024-clock-cv

## Итерация 2

### [Презентация итогов 2-oй итерации](https://github.com/moevm/mse1h2024-clock-cv/blob/pres/presentation/2.pdf)
### [Запись экрана с демонстрацией работы приложения](https://disk.yandex.ru/i/e3DCrIg64epaPw)


## Итерация 3

### [Презентация итогов 3-oй итерации](https://github.com/moevm/mse1h2024-clock-cv/blob/pres/3.pdf)
### [Запись экрана с демонстрацией работы приложения](https://disk.yandex.ru/i/aIh6jxcVMF2kIg)

## Итерация 4

### [Презентация итогов 4-oй итерации](https://github.com/moevm/mse1h2024-clock-cv/blob/main/presentation/4.pdf)
### [Тестовые изображения для проверки работоспособности приложения](https://github.com/moevm/mse1h2024-clock-cv/tree/main/clockcv-backend/clockcv/CV/test_image)
### [Тесты, проверяющие работоспособность приложения](https://github.com/moevm/mse1h2024-clock-cv/tree/main/tests)

### Руководство по запуску:

Для запуска требуется [Docker](https://www.docker.com/products/docker-desktop/)


1. Переместиться в директорию deploy
2. `docker-compose -f docker-compose.dev.yml build --no-cache` - создание контейнеров.
3. `docker-compose -f docker-compose.dev.yml up --force-recreate --remove-orphans` - запуск контейнеров(может не собраться с 1-го раза из-за большого количества файлов (зависимостей), так что следует несколько раз его запускать при возникновении ошибок).
4. После того, как увидите в терминале строку `backend   | INFO:     Application startup complete.`, перейдите по ссылке "http://localhost:8080" в своем браузере, чтобы открыть веб-интерфейс приложения.

### Инструкция по использованию приложения:

При переходе по ссылке открывается страница авторизации. Для пользователя доступно несколько вариантов действий:
- Вход в систему
- Регистрация 
- Восстановление пароля
- Гостевой вход (ограничивает возможности функционала приложения)

Далее открывается страница с тестированием. Для прохождения теста вам необходимо скачать макет и нарисовать часы согласно инструкции, после этого вы должны загрузить ваш рисунок. Для зарегистрированных пользователей также доступен переход на страницу истории. Нажав на кнопку результат, вы перейдете на страницу и перед вами появится количество баллов с текстовым и визуальным пояснением ваших ошибок.

В случае, если пользователь вошел в систему, будет доступна страница с историей тестирования (для неавторизированных пользователей кнопка перехода на эту страницу неактивна), которая будет включать информацию о каждом прохождении теста: дата прохождения и результат, кнопка, при нажатии на которую будут видны комментарии по поводу конкретного прохождения. На данной странице расположена кнопка график, при нажатии на которую пользователь перейдет на страницу с графиками, где будет с помощью гистограмм указана динамика результатов прохождений пользователя.

### Руководство по тестам

Для того, чтоб запустить тесты, нужно перейти в папку tests. 

#### Руководство по локальному запуску

##### Запустить веб приложение

Необходимо запустить приложение согласно руководству по запуску в файле README.md в корне проекта.


##### Установить зависимости

```
pip install -r requirements.txt
```

##### Запустить тесты

```
python ./basic_test.py
```

Тесты проверяют работоспособность кнопок на сайте, служат для нахождения конфликтов в pull request