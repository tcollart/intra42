# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20150203_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 3, 23, 52, 30, 636067)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='validated_by',
            field=models.ForeignKey(default=None, blank=True, related_name='TicketValidatedBy', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticketanswer',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 3, 23, 52, 30, 636742)),
            preserve_default=True,
        ),
    ]
