# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_inscripciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripciones',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=2, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='cedula',
            field=models.IntegerField(),
        ),
    ]
