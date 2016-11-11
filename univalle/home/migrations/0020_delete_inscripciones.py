# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20161110_1658'),
    ]

    operations = [
        migrations.DeleteModel(
            name='inscripciones',
        ),
    ]
