# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0072_auto_20161201_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listado_admitidos',
            name='puntaje',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='programasacademico',
            name='competencias_ciudadanas',
            field=models.IntegerField(),
        ),
    ]
