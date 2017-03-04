## Install libraries

`pip install -r requirements.txt`

For now the project uses Python 2.7, be aware of possible issues if you have Python 3.

## Test locally

You can pick either SQLite or MySQL for local testing.

### SQLite

No need to do anything, but since our Google cloud app uses MySQL, be aware of possible inconsistencies.

### MySQL

`sudo apt-get update`

`sudo apt-get install libmysqlclient-dev mysql-client mysql-server`

If it is your first time to install `mysql-server`, a prompt should appear to ask you to set up the root password.

Start your local MySQL service:

`service mysql restart`

By default, the service runs on port 3306.
Check if the MySQL service is running:

`ps aux | grep mysqld`

Check if you can connect to your local MySQL server using root:

`mysql -u root -p` then enter the root password.

If you have not created the local MySQL database:
`CREATE DATABASE catalyst;`

Uncomment the MySQL local service part in the `DATABASES` entry in `civic_marketplace/settings.py`. Put your root password there.

### Populate the database

`python manage.py makemigrations dashboard account
python manage.py migrate
python manage.py loaddata skills causes organizations preferredtimes
`

Check if django tables are created in your selected backend.

If you met any migration problem and had to clean up everything, here is a [tutorial](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html) on how to reset migrations. Be aware that you will lose all the data by doing this. It happens when old migration scripts are not applicable to the new schema.

### Run the server on localhost

`python manage.py runserver`

Then check the website in localhost:8000.

You can also do:

`python manage.py runserver host:port`

but may need to add the `host` in `ALLOWED_HOSTS` in `civic_marketplace/settings.py`.

## Connect to Google Cloud Platform

`./cloud_sql_proxy -instances="catalyst-market:us-central1:catalyst"=tcp:3307`

This launches a local service listening on 3307, which connects to our instance on Google Cloud Platform.
Change the port number if needed.

To connect to the local service **and thus also our cloud instance**, run:

`mysql -h 127.0.0.1 --port 3307 -u catalyst -p` then enter `catalyst` as the password.

Notice: **ALL CHANGES MADE HERE APPLY TO OUR CLOUD INSTANCE**

## Deploy to Google Cloud Platform

Install Cloud SDK: https://cloud.google.com/sdk/downloads

To include third-party libraries:

`pip install -t lib/ django google-cloud django-social-auth`

Collect static files:

`python manage.py collectstatic`

Finally, deploy it:

`gcloud app deploy --project catalyst-market`

Notice: **THIS DEPLOYS A NEW VERSION TO GOOGLE CLOUD**

## Admin account

Admin URI: https://catalyst-market.appspot.com/admin

username: catalyst

password: catalyst

