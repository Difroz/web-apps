Приложение по обработке информации о продажах
Обрабатывает информацию из csv файла, сохраняет ее в БД и возвращает список из 5 пользователей


Как начать работу с приложением:

1) Установить Docker— https://docs.docker.com/get-docker/

1.1) Установить docker-compose — https://docs.docker.com/compose/install/

2.) Сделать клон git репозитория — https://github.com/42musaev/bobcat_lms

3.) В директории проекта запустить docker-compose up --build
4.) В командной строке контейнера ввести команды:
python manage.py makemigrations
python manage.py migrate

4.)Перейти по ссылке http://localhost:8000/deals-api/ и загузить csv файл

