# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_delete_inscripciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='inscripciones',
            fields=[
                ('cedula', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('snp', models.CharField(max_length=50)),
                ('carrera', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
