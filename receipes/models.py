from django.db import models
from django.conf import settings

class User(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)

class Ingredient(models.Model):
    name_ingredient = models.CharField(max_length=100)
    note = models.CharField(max_length=1000)
    
class Recipe(Ingredient):
    pass
        
class Dish(Recipe):
    book = models.ManyToManyField('Book')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    type = models.ForeignKey('DishType')
    
class DishType(models.Model):    
    name_type = models.CharField(max_length=100)
    
class RecipePart(models.Model):
    recipe = models.ForeignKey('Recipe')
    ingredient = models.ForeignKey('Ingredient')
    unit = models.CharField(max_length=100)
    note = models.CharField(max_length=100)