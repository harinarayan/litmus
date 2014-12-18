# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rip', '0005_auto_20141218_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='sample_json',
            field=models.TextField(max_length=400000),
            preserve_default=True,
        ),
    ]
