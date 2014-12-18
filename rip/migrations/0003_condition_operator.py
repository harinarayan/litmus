# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rip', '0002_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='operator',
            field=models.CharField(default=b'EQ', max_length=19, choices=[(b'EQ', b'EQ'), (b'NE', b'NE'), (b'IN', b'IN'), (b'NI', b'NOT IN')]),
            preserve_default=True,
        ),
    ]
