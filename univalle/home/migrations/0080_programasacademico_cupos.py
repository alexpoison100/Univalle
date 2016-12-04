# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0079_delete_listado_admitidos'),
    ]

    operations = [
        migrations.AddField(
            model_name='programasacademico',
            name='cupos',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
