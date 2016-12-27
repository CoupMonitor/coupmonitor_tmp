# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocationTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('governorate', models.CharField(max_length=300)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='locations.Location', null=True)),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'locations_location_translation',
                'db_tablespace': '',
            },
        ),
        migrations.AlterUniqueTogether(
            name='locationtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
