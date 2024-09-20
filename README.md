# Django config & launch

## Py config

```sh
python -m venv env
source env/bin/activate
pip install django
pip freeze > requirements.txt
```

## Django init

```sh
django-admin startproject lycaste
cd lycaste
```
Now that it has been initialized, let's launch it

Database creation:

```sh
python manage.py migrate
```

This creates db.sqlite3. It can be opened with DBeaver.

Let's create an application. A web project can be made of several applications.

```sh
python manage.py startapp main
```

The app should be added into lycaste/lycaste/settings.py

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main', # <- here
]
```

## MVT: Models, Views, Templates

Views are website pages. They are added in the appli /views.py & in the project urls.py.

Models are both SQL entries and Python classes. In other terms, they allow for permanent objects.

Templates are html pre-formatted pages.

## Migrations

We have created a new model, therefore the database needs a new table.

Still from lycaste:

```sh
python manage.py makemigrations
python manage.py migrate
```
## Django CLI or shell

This is actually a python CLI.

```sh
python manage.py shell
```

## Launch server

```sh
python manage.py runserver
```

## Admin

Create a superuser:

```sh
python manage.py createsuperuser
```

Admin board is now available at lycaste.eu/admin

## Dockerization

The project is dockerized using docker-compose.

- The PostgreSQL data base runs as a service.
- The Django app runs as a service.

2 important folders are not gitted:

- .env contains all secrets (db & django app credentials). It looks like:

```sh
POSTGRES_DB=db_prod
POSTGRES_USER=admin
POSTGRES_PASSWORD=qwerty
DJANGO_SECRET_KEY=12345
```

- data contains 2 subfolders:
    - db, which is the database volume ;
    - img, with all graphical resources needed for the website.

These files need to be manually added & updated to the VPS environment.

The app is built & launched using:

```sh
docker-compose build
docker-compose up
```

To manage the django app, it is required to enter within the webapp container. First identify the webapp container id:

```sh
docker ps
```

Say "id123", then:

```sh
docker exec -it id123 bash
```

to enter the container from which `python manage.py` commands may be launched.

## create email user

from within the smtp container:

```sh
saslpasswd2 -c -u lycaste.eu "admin" <<< "qwerty" # use actual password instead
```

## create ssl keys

```sh
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d lycaste.eu -d www.lycaste.eu -d mail.lycaste.eu
```

## Database access

The database may be accessed from lycaste.eu/admin, using the right credentials ; or from DBeaver from one of the few IPs that are allowed to access port 5432 in the UFW configuration.

## License

This project and embedded resources are copyrighted and the property of their author.