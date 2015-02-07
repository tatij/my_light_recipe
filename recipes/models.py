from django.db import models
from django.conf import settings


class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=1000)


class Dish(Ingredient):
    book = models.ManyToManyField('Book')
    verbose_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    type = models.ForeignKey('DishType')
    photo = models.ImageField(null=True, blank=True)


class DishType(models.Model):    
    name_type = models.CharField(max_length=100)
    parent = models.ForeignKey('self')


class RecipePart(models.Model):
    recipe = models.ForeignKey('Ingredient', related_name='recipe_component')
    ingredient = models.ForeignKey('Ingredient')
    unit = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    amount = models.IntegerField()


class Action(models.Model):
    name = models.CharField(max_length=128)


class RecipeAction(models.Model):
    recipe = models.ForeignKey('RecipePart')
    action = models.ForeignKey('Action')
    comment = models.TextField()