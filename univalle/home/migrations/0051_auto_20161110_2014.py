# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_auto_20161110_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripciones',
            name='cedula',
            field=models.BigIntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
