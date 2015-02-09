# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20150203_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='creation_date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticketanswer',
            name='creation_date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
