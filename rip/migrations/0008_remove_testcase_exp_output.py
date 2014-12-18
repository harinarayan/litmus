# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rip', '0007_auto_20141218_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcase',
            name='exp_output',
        ),
    ]
