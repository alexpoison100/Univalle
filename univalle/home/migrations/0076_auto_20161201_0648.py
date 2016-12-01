# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0075_auto_20161201_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programasacademico',
            name='competencias_ciudadanas',
            field=models.FloatField(),
        ),
    ]
