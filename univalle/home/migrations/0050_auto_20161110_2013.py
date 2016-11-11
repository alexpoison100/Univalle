# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_auto_20161110_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripciones',
            name='id',
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='cedula',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
    ]
