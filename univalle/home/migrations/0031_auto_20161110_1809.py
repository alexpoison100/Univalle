# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20161110_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripciones',
            name='cedula',
            field=models.BigIntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
