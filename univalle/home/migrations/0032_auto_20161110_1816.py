# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20161110_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscripciones',
            old_name='cedula',
            new_name='id',
        ),
    ]
