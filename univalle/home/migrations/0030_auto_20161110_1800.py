# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20161110_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripciones',
            name='id',
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='cedula',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
