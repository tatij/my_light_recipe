"""
This is example how to use postgresql DB local settings
Rename _local_settings.py to local_settings.py locally
change DB_NAME, DB_USER as you wish, enjoy


To create DB on ubuntu, login to psql console:
sudo -u postgres psql
>
> CREATE DATABASE light_recipe;
> CREATE USER developer WITH PASSWORD '123456';
> GRANT ALL PRIVILEGES ON DATABASE light_recipe TO developer;
> ALTER USER developer WITH SUPERUSER;
> \q

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'light_recipe',
        'USER': 'developer',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
