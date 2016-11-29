# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_auto_20161125_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listado_admitidos',
            name='id',
            field=models.AutoField(unique=True, serialize=False, primary_key=True),
        ),
    ]
