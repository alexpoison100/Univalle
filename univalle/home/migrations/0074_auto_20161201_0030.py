# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0073_auto_20161201_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='listado_admitidos',
            name='id',
            field=models.AutoField(default=2, unique=True, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listado_admitidos',
            name='cedula',
            field=models.IntegerField(),
        ),
    ]
