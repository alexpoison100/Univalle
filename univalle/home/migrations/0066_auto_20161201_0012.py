# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0065_auto_20161130_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listado_admitidos',
            name='id',
        ),
        migrations.AddField(
            model_name='listado_admitidos',
            name='cedula',
            field=models.BigIntegerField(default=95234123, unique=True, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
