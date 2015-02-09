# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=10000)),
                ('creation_date', models.DateField(default=datetime.datetime(2015, 2, 3, 23, 41, 14, 828496))),
                ('resolved', models.BooleanField(default=False)),
                ('validated_at', models.DateField(blank=True)),
                ('validated_by', models.ForeignKey(related_name='TicketValidatedBy', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TicketAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('message', models.TextField(max_length=10000)),
                ('creation_date', models.DateField(default=datetime.datetime(2015, 2, 3, 23, 41, 14, 829082))),
                ('author', models.ForeignKey(related_name='TicketAnswerAuthor', to=settings.AUTH_USER_MODEL)),
                ('ticket_related', models.ForeignKey(related_name='TicketAnswer', to='tickets.Ticket')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
