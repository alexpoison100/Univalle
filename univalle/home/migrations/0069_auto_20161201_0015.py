# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0068_auto_20161201_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='listado_admitidos',
            name='cedula',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listado_admitidos',
            name='id',
            field=models.AutoField(unique=True, serialize=False, primary_key=True),
        ),
    ]
