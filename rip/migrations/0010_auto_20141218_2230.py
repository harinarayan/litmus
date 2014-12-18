# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rip', '0009_auto_20141218_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='input',
            field=models.TextField(default=b'{}', max_length=400000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='url_kwargs',
            field=models.TextField(default=b'{}', max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcase',
            name='url_params',
            field=models.TextField(default=b'{}', max_length=3000, null=True),
            preserve_default=True,
        ),
    ]
