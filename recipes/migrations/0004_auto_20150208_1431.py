# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20150207_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.CharField(max_length=1024, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dish',
            name='verbose_name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dishtype',
            name='name_type',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='note',
            field=models.CharField(max_length=1024, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipeaction',
            name='comment',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipepart',
            name='note',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipepart',
            name='unit',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
