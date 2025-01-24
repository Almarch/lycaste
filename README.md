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
## Django CLI or shell

This is actually a python CLI.

```sh
python manage.py shell
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
sudo chmod -R 755 data
```

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
docker-compose exec mailserver setup email add user@lycaste.eu
docker-compose exec mailserver setup email list
```

It is important to well parameterize the SPF so that the mails are not red-flagged (see [OVH documentation](https://help.ovhcloud.com/csm/fr-dns-spf-record?id=kb_article_view&sysparm_article=KB0051712)) ; and to make sure the domain links to the IP with no competition with for instance OVH mail hosting services.

## create ssl keys

```sh
sudo apt install snapd
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot certonly --nginx -d lycaste.eu -d www.lycaste.eu -d mail.lycaste.eu -d dev.lycaste.eu
```

These keys are then placed into /etc/letsencrypt. They are used by nginx and the mailserver.

## email access

New mailbox on thunderbird :

![image](https://github.com/user-attachments/assets/b1b00727-ffe9-4986-a4cb-ccdd5a1f7537)

## Database access

The database may be accessed from lycaste.eu/admin, using the right credentials ; or from DBeaver from one of the few IPs that are allowed to access port 5432 in the UFW configuration.

## License

This project and embedded resources are copyrighted and the property of their author.
