from django.db import models

class User(models.Model):
    id_user = models.ForeignKey('Book')
    name_user = models.CharField(max_length=100)

class Book(models.Model):
    id_book = models.ForeignKey('ConnectDishBook')
    id_user = models.ForeignKey('User')
    name_book = models.CharField(max_length=100)
    
class ConnectDishBook(models.Model):
    id = models.IntegerField(default=0)
    id_book = models.ForeignKey('Book')
    id_dish_connect = models.ForeignKey('Dish')
    
class Dish(models.Model):
    id_dish_connect = models.ForeignKey('ConnectDishBook')
    id_dish_recipe = models.ForeignKey('Recipe')
    name_dish = models.CharField(max_length=100)
    id_book = models.IntegerField(default=0)
    type_dish = models.ForeignKey('DishType')
    description = models.CharField(max_length=1000)
    
class DishType(models.Model):
    id_type = models.ForeignKey('Dish')
    name_type = models.CharField(max_length=100)
    
class Recipe(models.Model):
    id_recipe = models.ForeignKey('RecipePart')
    id_ingredient = models.ForeignKey('Ingredient')
    id_dish_recipe = models.ForeignKey('Dish')
    
class RecipePart(models.Model):
    id_recipe = models.ForeignKey('Recipe')
    id_ingredient = models.ForeignKey('Ingredient')
    unit = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    
class Ingredient(models.Model):
    id_ingredient = models.ForeignKey('RecipePart')
    name_ingredient = models.CharField(max_length=100)
    note = models.CharField(max_length=1000)