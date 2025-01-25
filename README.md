# Django config & 

## Migrations

from the bash of django container:

```sh
 docker exec -it id123 bash
```

```sh
python manage.py makemigrations authentication
python manage.py makemigrations main
python manage.py migrate
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

- .env contains all secrets (db & django app credentials) and the environment info (prod/dev). It looks like:

```sh
ENVIRONMENT=prod
POSTGRES_DB=db_prod
POSTGRES_USER=admin
POSTGRES_PASSWORD=123
DJANGO_SECRET_KEY=abc
POSTGRES_PORT_MAPPING="123:123"
```

- data which is made as such:

```sh
mkdir data
mkdir data/db
mkdir data/img
mkdir data/migrations
mkdir data/migrations/main
mkdir data/migrations/authentication
mkdir data/mailserver
mkdir data/mailserver/mail-data
mkdir data/mailserver/mail-state
mkdir data/mailserver/mail-logs
mkdir data/mailserver/config
mkdir data/certbot
mkdir data/certbot/www
mkdir data/certbot/conf
mkdir data/wordpress
mkdir data/wordpress/db
mkdir data/wordpress/content
sudo chmod -R 755 data
```

These files need to be manually added to the VPS environment.

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
docker-compose exec mailserver setup email add user@lycaste.eu
docker-compose exec mailserver setup email list
```

It is important to well parameterize the SPF so that the mails are not red-flagged (see [OVH documentation](https://help.ovhcloud.com/csm/fr-dns-spf-record?id=kb_article_view&sysparm_article=KB0051712)) ; and to make sure the domain links to the IP with no competition with for instance OVH mail hosting services.

## create ssl keys

In order to generate the keys, use the dedicated service:

```sh
docker-compose run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ -d lycaste.eu -d www.lycaste.eu -d mail.lycaste.eu -d draft.lycaste.eu -d dev.lycaste.eu --force-renewal
```

## email access

New mailbox on thunderbird :

![image](https://github.com/user-attachments/assets/b1b00727-ffe9-4986-a4cb-ccdd5a1f7537)

## Wordpress

A wordpress image is also used in order to support the website design, at the adress draft.lycaste.eu. It is behind ufw and only a few IPs have access to it.

## Database access

The database may be accessed from lycaste.eu/admin, using the right credentials ; or from DBeaver from one of the few IPs that are allowed to access port 5432 in the UFW configuration.

## License

This project and embedded resources are copyrighted and the property of their author.
