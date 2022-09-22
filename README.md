## Проект "Отзывы об автомобилях"

### Технологии:

Python, Django, Django Rest Framework, Docker, PostgreSQL

### Развернуть проект на локальной машине:

- Клонировать репозиторий:
```
https://github.com/mikhailsoldatkin/car_reviews.git
```

- Создать и запустить контейнеры Docker, выполнить команду (находясь в папке car_reviews):
```
docker-compose up -d
```

- Создать суперпользователя, указать имя, пароль и email:
```
docker-compose exec backend python manage.py createsuperuser
```

- После запуска проект будут доступен по адресу: [http://localhost/](http://localhost/)


- Для остановки контейнеров Docker:
```
docker-compose down -v      # с их удалением
docker-compose stop         # без удаления
```

- Для тестирования API через Postman:
```
в коллекции Postman импортировать файл postman_collection.json
```

### Автор

Михаил Солдаткин (c) 2022
