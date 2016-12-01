# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0078_auto_20161201_1357'),
    ]

    operations = [
        migrations.DeleteModel(
            name='listado_admitidos',
        ),
    ]
