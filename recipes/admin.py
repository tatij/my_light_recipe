from django.contrib import admin
from .models import *

admin.site.register(Ingredient)
admin.site.register(Book)
admin.site.register(Dish)
admin.site.register(DishType)
admin.site.register(RecipePart)
admin.site.register(Action)
admin.site.register(RecipeAction)
