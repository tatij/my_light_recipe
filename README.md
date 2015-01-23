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

```

###4.Check if dev server starts as well:  
```
 python light_recipe/manage.py runserver
```

