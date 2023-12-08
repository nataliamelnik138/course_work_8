# Трекер полезных привычек

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)

### Технологии:
- Python 3.11
- Django 4.2.2
- Django REST framework 3.14.0
- PostgreSQL
- Celery 5.3.5
- Redis 5.0.1
- Docker

### Инструкция по развертыванию проекта:

#### Клонирование проекта:
```
git clone https://github.com/nataliamelnik138/course_work_7
```
#### Запуск проекта с использованием Docker:
Запустите контейнер
```
docker-compose up -d —build 
```

#### Запуск проекта без использования Docker:
Запуск:
1. Создайте виртуальное окружение
```
python -m venv venv
```
2. Активируйте виртуальное окружение
```
venv/Skripts/activate
```
4. Установите зависимости
```
pip install -r requirements.txt
```
6. Создайте в папке проекта файл .env, который должен содержать значение переменных из файла .env.sample
7. Примените миграции
```
python manage.py migrate
```
6. Запустите проект
```
python manage.py runserver
```
Запуск периодической задачи отправки в чат Telegram напоминания о выполнении привычки: 
```
celery -A config worker -l INFO -P eventlet    
```
```
celery -A config  beat -l info 
```

### Документация API
```
http://127.0.0.1:8000/redoc/
```

#### Автор проекта: Мельник Наталья
