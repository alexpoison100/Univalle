# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0076_auto_20161201_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='lista_admitidos',
            fields=[
                ('cedula', models.BigIntegerField(unique=True, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('puntaje', models.FloatField()),
                ('carrera', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
