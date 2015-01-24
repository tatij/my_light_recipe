### my_light_recipe
To start dev process on Ubuntu 14.04:  

###1.Clone git project.
```
$ git clone git@github.com:tatij/my_light_recipe.git
$ cd my_light_recipe
```

###2.Make local settings  
2.1 Copy light_recipe/_local_settings.py to light_recipe/local_settings.py.  
2.2 Go trought example in docstring to setup local DB settings.  
2.3 Create DB in postgresql.  

###3.Create local virtualenv.  
```
$ cd my_light_recipe
$ pyvenv-3.4 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
... installation process
$ python manage.py syncdb
```

###4.Check if dev server starts as well:  
4.1 If you want to use django dev server:
```
(venv)$ python manage.py runserver
```
Your app should be on http://localhost:8000

4.2 If you have heroku installed, you can use foreman
```
$ foreman start web
```
Your app should now be running on [localhost:5000](http://localhost:5000/).


###5.Deploying to Heroku

```
$ heroku create
$ git push heroku master
$ heroku run python manage.py syncdb
$ heroku open
```

