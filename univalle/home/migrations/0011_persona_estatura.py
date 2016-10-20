# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='estatura',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
