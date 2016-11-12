# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0054_auto_20161111_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripciones',
            name='ref_pago',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
