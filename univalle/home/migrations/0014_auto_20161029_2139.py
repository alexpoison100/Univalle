# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_programasacademico_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programasacademico',
            name='id',
        ),
        migrations.AlterField(
            model_name='programasacademico',
            name='codigo',
            field=models.BigIntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
