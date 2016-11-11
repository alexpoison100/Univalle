# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20161110_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripciones',
            name='carrera',
            field=models.CharField(max_length=200),
        ),
    ]
