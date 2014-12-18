# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rip', '0003_condition_operator'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='method',
            field=models.CharField(default=b'GET', max_length=7, choices=[(b'GET', b'GET'), (b'POST', b'POST'), (b'PUT', b'PUT'), (b'DELETE', b'DELETE'), (b'HEAD', b'HEAD'), (b'OPTIONS', b'OPTIONS'), (b'PATCH', b'PATCH')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcase',
            name='url_kwargs',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcase',
            name='url_params',
            field=models.CharField(max_length=3000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condition',
            name='field',
            field=models.CharField(max_length=10000, null=True),
            preserve_default=True,
        ),
    ]
