# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_delete_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='programasacademico',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
