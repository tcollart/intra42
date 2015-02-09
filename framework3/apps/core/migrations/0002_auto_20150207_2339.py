# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=12, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(null=True, upload_to='', blank=True),
            preserve_default=True,
        ),
    ]
