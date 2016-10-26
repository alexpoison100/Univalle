# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_programas'),
    ]

    operations = [
        migrations.AddField(
            model_name='programas',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
