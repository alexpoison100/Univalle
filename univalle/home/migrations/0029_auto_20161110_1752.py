# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20161110_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripciones',
            name='status',
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='carrera',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
    ]
