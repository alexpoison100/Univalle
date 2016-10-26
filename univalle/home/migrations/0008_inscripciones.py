# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20161015_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='inscripciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('snp', models.CharField(max_length=50)),
                ('carrera', models.CharField(max_length=100)),
            ],
        ),
    ]
