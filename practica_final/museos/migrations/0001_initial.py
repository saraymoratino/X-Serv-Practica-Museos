# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('usuario', models.TextField()),
                ('fecha', models.TextField()),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='museos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('museo', models.TextField()),
                ('id_entidad', models.TextField()),
                ('descripcion', models.TextField()),
                ('horario', models.TextField()),
                ('transporte', models.TextField()),
                ('accesibilidad', models.TextField()),
                ('content_url', models.TextField()),
                ('nombre_via', models.TextField()),
                ('clase_vial', models.TextField()),
                ('tipo_num', models.TextField()),
                ('num', models.TextField()),
                ('localidad', models.TextField()),
                ('provincia', models.TextField()),
                ('codigo_postal', models.TextField()),
                ('barrio', models.TextField()),
                ('distrito', models.TextField()),
                ('coordenada_x', models.TextField()),
                ('coordenada_y', models.TextField()),
                ('latitud', models.TextField()),
                ('longitud', models.TextField()),
                ('telefono', models.TextField()),
                ('fax', models.TextField()),
                ('email', models.TextField()),
                ('tipo', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='museo',
            field=models.ForeignKey(to='museos.museos'),
        ),
    ]
