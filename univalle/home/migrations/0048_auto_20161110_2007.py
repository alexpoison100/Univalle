# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_auto_20161110_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripciones',
            name='cedula',
            field=models.BigIntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
