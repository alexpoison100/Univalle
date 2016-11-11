# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20161110_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripciones',
            name='id',
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='cedula',
            field=models.BigIntegerField(default=0, unique=True, serialize=False, primary_key=True),
        ),
    ]
