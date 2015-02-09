# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0008_auto_20150203_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='assigned_to',
            field=models.ForeignKey(help_text='Assign the ticket to an admin', null=True, blank=True, to=settings.AUTH_USER_MODEL, default=None, related_name='TicketAssignedTo'),
            preserve_default=True,
        ),
    ]
