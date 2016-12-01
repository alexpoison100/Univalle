# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0077_lista_admitidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripciones',
            name='competencias_ciudadanas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='ingles',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='lectura_critica',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='matematicas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='naturales',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='razonamiento_cuantitativo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='sociales',
            field=models.IntegerField(),
        ),
    ]
