# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20161029_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripciones',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
