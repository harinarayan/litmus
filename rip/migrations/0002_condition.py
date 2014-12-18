# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field', models.CharField(max_length=10000)),
                ('value', models.CharField(max_length=1000)),
                ('testcase', models.ForeignKey(to='rip.TestCase')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
