# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm_events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventOrganizers',
            field=models.ForeignKey(to='cm_events.EventOrganizer', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventSize',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='resource',
            field=models.ForeignKey(to='archive.Resource', null=True),
        ),
    ]
