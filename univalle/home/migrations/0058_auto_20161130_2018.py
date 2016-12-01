# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0057_auto_20161125_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripciones',
            name='colegio',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='competencias_ciudadanas',
            field=models.IntegerField(default=44),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='ingles',
            field=models.IntegerField(default=95),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='lectura_critica',
            field=models.IntegerField(default=44),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='matematicas',
            field=models.IntegerField(default=92),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='naturales',
            field=models.IntegerField(default=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='razonamiento_cuantitativo',
            field=models.IntegerField(default=49),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='sociales',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='competencias_ciudadanas',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='info',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='ingles',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='lectura_critica',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='matematicas',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='naturales',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='razonamiento_cuantitativo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='sociales',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
