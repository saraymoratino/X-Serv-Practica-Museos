# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='museos',
            old_name='tipo',
            new_name='descripcion_entidad',
        ),
    ]
