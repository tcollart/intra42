# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_auto_20150203_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='validated_at',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
