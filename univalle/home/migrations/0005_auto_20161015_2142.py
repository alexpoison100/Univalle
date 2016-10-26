# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20161015_2139'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='programas',
            new_name='programasAcademicos',
        ),
    ]
