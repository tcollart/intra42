# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_ticket_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assigned_to',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, help_text='Assign the ticket to an admin', related_name='TicketAssignedTo'),
            preserve_default=True,
        ),
    ]
