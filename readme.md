# Сервис по сбору вакансий

## Инструкция по запуску:
* ### Склонировать репозиторий: ``git clone``
* ### Создать виртуальное окружение: ``python -m venv venv``
* ### Установить все зависимости: ``pip install -r req.txt``
* ### Выполнить миграции: ``manage.py makemigrations``, затем ``manage.py migrate``
* ### Создать супер-пользователя: ``manage.py createsuperuser``
* ### Запустить проект: ``manage.py runserver``

## Используемая технология:
* ### Django
* ### Asyncio
* ### BeautifulSoup
* ### Requests