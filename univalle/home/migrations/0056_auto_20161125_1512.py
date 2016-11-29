# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0055_inscripciones_ref_pago'),
    ]

    operations = [
        migrations.CreateModel(
            name='listado_admitidos',
            fields=[
                ('id', models.BigIntegerField(unique=True, serialize=False, primary_key=True)),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('puntaje', models.IntegerField()),
                ('carrera', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='programasacademico',
            name='puntaje_min',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
