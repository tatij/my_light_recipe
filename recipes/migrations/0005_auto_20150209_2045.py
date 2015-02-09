# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20150208_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(upload_to='', null=True, blank=True),
            preserve_default=True,
        ),
    ]
