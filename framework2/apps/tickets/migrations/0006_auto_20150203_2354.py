# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20150203_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 3, 23, 54, 1, 282992)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticketanswer',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 3, 23, 54, 1, 283601)),
            preserve_default=True,
        ),
    ]
