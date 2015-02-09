# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_basecategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basepost',
            name='message',
            field=models.TextField(max_length=10000),
            preserve_default=True,
        ),
    ]
