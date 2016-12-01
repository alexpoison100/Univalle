# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0058_auto_20161130_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripciones',
            name='competencias_ciudadanas',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='ingles',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='lectura_critica',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='matematicas',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='naturales',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='razonamiento_cuantitativo',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='sociales',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='programasacademico',
            name='competencias_ciudadanas',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='programasacademico',
            name='ingles',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='programasacademico',
            name='lectura_critica',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='programasacademico',
            name='matematicas',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='programasacademico',
            name='naturales',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='programasacademico',
            name='razonamiento_cuantitativo',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='programasacademico',
            name='sociales',
            field=models.FloatField(),
        ),
    ]
