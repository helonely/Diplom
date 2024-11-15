[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/-DRF-464646?style=flat-square&logo=django)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![PEP 8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.0.0-yellowgreen.svg)](https://swagger.io/specification/)
[![Docker](https://img.shields.io/badge/Docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/)

DF1.
### REST API для управления библиотекой - это веб-приложение,
построенное с использованием Django Rest Framework (DRF),
которое предоставляет функции для управления книгами,
авторами и пользователями в библиотеке. 

### Вот краткое описание проекта:
## Основные возможности
### Управление книгами:
    Создание, редактирование и удаление книг
    Получение списка всех книг
    Поиск книг по различным критериям (название, автор, жанр и т.д.)
### Управление авторами:
    Создание, редактирование и удаление авторов
    Получение списка всех авторов
### Управление пользователями:
    Регистрация и авторизация пользователей
    Получение информации о пользователях
### Выдача книг:
    Запись информации о выдаче книги пользователю
    Отслеживание статуса возврата книги
### Технические детали
    Фреймворк: Django Rest Framework (DRF)
    База данных: PostgresSQL
    Контейнеризация: Docker и Docker Compose
    Документация API: OpenAPI (автогенерируемая)
    Стандартизация кода: PEP8

### Инструкция:
## Установка
1. Клонируйте репозиторий:
    git clone https://github.com/helonely/Diplom.git
2. Активируйте виртуальное окружение:
    python -m venv env
    source env/bin/activate  # на Unix или MacOS
    env\Scripts\activate.bat  # на Windows
3. Убедитесь, что Docker установлен на ваш компьютер, или установите из дистрибутива, полученного на сайте https://www.docker.com/. 

4. Для запуска процесса создания контейнеров в терминале перейдите в корневую папку проекта и выполните команду:
    $ docker-compose up -d --build

5. После завершения процесса развертывания и запуска приложений в контейнерах docker к приложению можно обращаться через http://localhost:8000/

6. В браузере по адресу http://localhost:8000/swagger/ можно ознакомиться с описанием API.

### Авторы
SKYPRO,
https://github.com/helonely - разработчик проекта.
