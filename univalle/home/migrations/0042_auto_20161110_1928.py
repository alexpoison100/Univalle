# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_auto_20161110_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aspirantes',
            name='cedula',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
    ]
