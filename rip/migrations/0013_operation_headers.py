# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rip', '0012_service_protocol'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='headers',
            field=models.TextField(default=b'{"Content-Type":"application/json"}', max_length=1000),
            preserve_default=True,
        ),
    ]
