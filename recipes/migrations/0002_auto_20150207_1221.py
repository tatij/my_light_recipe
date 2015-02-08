# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='book',
            field=models.ManyToManyField(null=True, blank=True, to='recipes.Book'),
            preserve_default=True,
        ),
    ]
