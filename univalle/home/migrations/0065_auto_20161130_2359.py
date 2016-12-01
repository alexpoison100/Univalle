# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0064_auto_20161130_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listado_admitidos',
            name='cedula',
        ),
        migrations.AlterField(
            model_name='listado_admitidos',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
    ]
