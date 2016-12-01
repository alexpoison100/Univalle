# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0059_auto_20161130_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programasacademico',
            name='competencias_ciudadanas',
        ),
        migrations.RemoveField(
            model_name='programasacademico',
            name='ingles',
        ),
        migrations.RemoveField(
            model_name='programasacademico',
            name='lectura_critica',
        ),
        migrations.RemoveField(
            model_name='programasacademico',
            name='matematicas',
        ),
        migrations.RemoveField(
            model_name='programasacademico',
            name='naturales',
        ),
        migrations.RemoveField(
            model_name='programasacademico',
            name='razonamiento_cuantitativo',
        ),
        migrations.RemoveField(
            model_name='programasacademico',
            name='sociales',
        ),
    ]
