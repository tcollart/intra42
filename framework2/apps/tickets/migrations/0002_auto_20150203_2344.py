# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='author',
            field=models.ForeignKey(related_name='TicketAuthor', default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 3, 23, 44, 24, 765726)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticketanswer',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 3, 23, 44, 24, 766327)),
            preserve_default=True,
        ),
    ]
