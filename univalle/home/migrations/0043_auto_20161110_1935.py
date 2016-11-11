# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_auto_20161110_1928'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='aspirantes',
            new_name='inscripciones',
        ),
    ]
