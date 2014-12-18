# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rip', '0004_auto_20141218_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='field',
            field=models.CharField(default=datetime.datetime(2014, 12, 18, 13, 6, 32, 429034, tzinfo=utc), max_length=10000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='input',
            field=models.CharField(max_length=400000, null=True),
            preserve_default=True,
        ),
    ]
