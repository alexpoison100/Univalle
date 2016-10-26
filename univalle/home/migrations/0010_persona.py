# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_userprofile_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hojos', models.CharField(max_length=100)),
                ('piel', models.CharField(max_length=100)),
            ],
        ),
    ]
