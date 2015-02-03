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

### Social network secure keys
# twitter
#Go to https://apps.twitter.com/app/new and create the new application
#The callback URL should be something like http://test1.com:8000/complete/twitter/
SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''

#google OAuth2
#Go to https://console.developers.google.com/ and create a new application.
#Under APIs and Auth > Credentials, create a new Client ID.
#Make sure to specify the right callback URL: http://test1.com:8000/complete/google-oauth2/
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

#facebook
#Go to https://developers.facebook.com/apps/?action=create and click the green “Create New App” button.
#In the settings of the newly-created application, click “Add Platform”.
# From the options provided, choose Web,
# and fill in the URL of the site (http://test1.com:8000 in our example).
SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''

#VK
#http://psa.matiasaguirre.net/docs/backends/vk.html#oauth2
SOCIAL_AUTH_VK_OAUTH2_KEY = ''
SOCIAL_AUTH_VK_OAUTH2_SECRET = ''


#OK
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_KEY = ''
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_SECRET = ''
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_PUBLIC_NAME = ''

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_URL = '/'
