# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_programas_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programas',
            name='codigo',
            field=models.IntegerField(),
        ),
    ]
