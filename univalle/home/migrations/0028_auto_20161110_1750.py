# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20161110_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripciones',
            name='cedula',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='id',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
