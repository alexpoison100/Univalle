# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0060_auto_20161130_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='programasacademico',
            name='competencias_ciudadanas',
            field=models.FloatField(default=(0, 10)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='ingles',
            field=models.FloatField(default=(0, 10)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='lectura_critica',
            field=models.FloatField(default=(0, 15)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='matematicas',
            field=models.FloatField(default=(0, 30)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='naturales',
            field=models.FloatField(default=(0, 20)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='razonamiento_cuantitativo',
            field=models.FloatField(default=(0, 5)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='sociales',
            field=models.FloatField(default=(0, 10)),
            preserve_default=False,
        ),
    ]
