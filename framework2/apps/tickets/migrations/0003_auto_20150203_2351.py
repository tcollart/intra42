# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20150203_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 3, 23, 51, 34, 254755)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='validated_by',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='TicketValidatedBy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticketanswer',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 3, 23, 51, 34, 255431)),
            preserve_default=True,
        ),
    ]
