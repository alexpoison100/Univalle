# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_programasacademicos_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='programasAcademicos',
            new_name='programasAcademico',
        ),
    ]
