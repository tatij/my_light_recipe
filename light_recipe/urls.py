from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.views.generic import ListView
from recipes.models import Dish
from recipes.views import RecipeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'light_recipe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'cookbook.views.login'),
    url(r'^home/$', 'cookbook.views.home'),
    url(r'^done/$', 'cookbook.views.done', name='done'),
    url(r'^logout/$', 'cookbook.views.logout'),
    url(r'^signup/$', 'cookbook.views.signup', name="signup"),
    url(r'^email-sent/', 'cookbook.views.validation_sent'),
    url(r'^email/$', 'cookbook.views.require_email', name='require_email'),
    url(r'^add_dish/$', 'cookbook.views.add_dish', name='add_dish'),
    (r'^dish_list/$', ListView.as_view(model=Dish,)),

    (r'^details/(?P<dish_pk>\d+)/$', RecipeView.as_view()),


)

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

