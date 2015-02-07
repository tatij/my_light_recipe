# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DishType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name_type', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(to='recipes.DishType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('ingredient_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='recipes.Ingredient', auto_created=True, serialize=False)),
                ('verbose_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('book', models.ManyToManyField(to='recipes.Book')),
                ('type', models.ForeignKey(to='recipes.DishType')),
            ],
            options={
            },
            bases=('recipes.ingredient',),
        ),
        migrations.CreateModel(
            name='RecipeAction',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('action', models.ForeignKey(to='recipes.Action')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipePart',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('ingredient', models.ForeignKey(to='recipes.Ingredient')),
                ('recipe', models.ForeignKey(to='recipes.Ingredient', related_name='recipe_component')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recipeaction',
            name='recipe',
            field=models.ForeignKey(to='recipes.RecipePart'),
            preserve_default=True,
        ),
    ]
