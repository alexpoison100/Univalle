# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20161110_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripciones',
            name='cedula',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
