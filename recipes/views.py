__author__ = 'biceps'
from django.views.generic import TemplateView

from recipes.models import Dish


class RecipeView(TemplateView):

    template_name = "recipe_details.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if ('dish_pk' in context.keys() and
            Dish.objects.filter(pk=context['dish_pk']).count() == 1):
            dish = Dish.objects.get(pk=context['dish_pk'])
            ing = dish.ingredient_ptr
            context['dish'] = dish
            context['recipe_data'] = self.process_dish_data(ing)
        return self.render_to_response(context)

    def process_dish_data(self, ing):
        data = []

        for rp in ing.recipe_component.all():
            data.append(
                {'amount': rp.amount,
                 'unit': rp.unit,
                 'ingredient': rp.ingredient.name,
                 'actions': [i.action.name for i in rp.recipeaction_set.all()],
                 'components': self.process_dish_data(rp.ingredient)
                 }
            )
        return data








