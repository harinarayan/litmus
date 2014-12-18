# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rip', '0006_auto_20141218_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='input',
            field=models.TextField(max_length=400000, null=True),
            preserve_default=True,
        ),
    ]
