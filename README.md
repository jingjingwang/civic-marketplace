# A marketplace for social goods

## Install django

https://docs.djangoproject.com/en/1.10/intro/install/

For now the project uses Python 2.7 and django 1.10.

## Install MySQL

`pip install MySQL-python`

`sudo apt-get install libmysqlclient-dev mysql-client`

## Test locally

You can pick either SQLite or MySQL for local testing.

### SQLite

Change the `DATABASES` section in `civic_marketplace/settings.py` to use SQLite.

### MySQL

`sudo apt-get install mysql-server`

If you have not created the local MySQL database:
`
CREATE DATABASE catalyst;
CREATE USER '[MYSQL_USER]' IDENTIFIED BY '[MYSQL_PASSWORD]';
GRANT ALL ON *.* TO '[MYSQL_USER]';
`

Check if you can connect to your local MySQL server:

`mysql -h 127.0.0.1 --port 3306 -u [MYSQL_USER] -p` then enter `[MYSQL_PASSWORD]`

Change the `DATABASES` section in `civic_marketplace/settings.py` accordingly to use your username and password (and port number, if not 3306).

### Populate the database

`./populate.sh`

Check if django tables are created in your selected backend.

Edit `populate.sh` if necessary.

### Run the server on localhost

`python manage.py runserver`

The check the website in localhost:8000. 

You can also do:

`python manage.py runserver host:port`

but may need to add the `host` in `ALLOWED_HOSTS` in `civic_marketplace/settings.py`.

## Connect to Google Cloud Platform

`./cloud_sql_proxy -instances="catalyst-market:us-central1:catalyst"=tcp:3307`

This launches a local service listening on 3307, which connects to our instance on Google Cloud Platform.
Change the port number if needed.

To connect to the local service **and thus also our cloud instance**, run:

`mysql -h 127.0.0.1 --port 3307 -u [MYSQL_USER] -p` then enter `[MYSQL_PASSWORD]`

Notice: **ALL CHANGES MADE HERE APPLY TO OUR CLOUD INSTANCE**

## Deploy to Google Cloud Platform

`python manage.py collectstatic`

Install Cloud SDK: https://cloud.google.com/sdk/downloads

`gcloud app deploy --project catalyst-market`

Notice: **THIS DEPLOYS A NEW VERSION TO GOOGLE CLOUD**

## Test account

username: test

email: test@test

password: testtest
