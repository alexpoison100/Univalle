# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0066_auto_20161201_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listado_admitidos',
            old_name='cedula',
            new_name='id',
        ),
    ]
