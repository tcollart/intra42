# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20150203_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 3, 23, 53, 52, 964536)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticketanswer',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 3, 23, 53, 52, 965172)),
            preserve_default=True,
        ),
    ]
