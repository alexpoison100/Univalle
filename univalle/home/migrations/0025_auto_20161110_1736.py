# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20161110_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripciones',
            name='id',
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='cedula',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
