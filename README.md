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
