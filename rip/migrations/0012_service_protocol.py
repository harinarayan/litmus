# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rip', '0011_auto_20141219_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='protocol',
            field=models.CharField(default=b'HTTPS', max_length=5, choices=[(b'HTTP', b'HTTP'), (b'HTTPS', b'HTTPS')]),
            preserve_default=True,
        ),
    ]
