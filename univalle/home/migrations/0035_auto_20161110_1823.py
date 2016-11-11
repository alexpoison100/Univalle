# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20161110_1821'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='inscripcioness',
            new_name='inscripciones',
        ),
    ]
