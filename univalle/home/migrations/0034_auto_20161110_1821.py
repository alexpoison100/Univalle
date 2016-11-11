# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20161110_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='inscripcioness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.BigIntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('snp', models.CharField(max_length=50)),
                ('carrera', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='inscripciones',
        ),
    ]
