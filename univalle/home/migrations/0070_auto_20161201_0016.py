# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0069_auto_20161201_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listado_admitidos',
            name='id',
        ),
        migrations.AlterField(
            model_name='listado_admitidos',
            name='cedula',
            field=models.BigIntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
