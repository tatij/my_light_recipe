from django.contrib import admin
from .models import *
from sorl.thumbnail.admin import AdminImageMixin


class DishAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


admin.site.register(Ingredient)
admin.site.register(Book)
admin.site.register(Dish, DishAdmin)
admin.site.register(DishType)
admin.site.register(RecipePart)
admin.site.register(Action)
admin.site.register(RecipeAction)
