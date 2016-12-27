# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eventType', models.CharField(max_length=100)),
                ('eventSize', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('modifiedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.ForeignKey(to='cm_events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventOrganizer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventOrganizerTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organizerName', models.TextField()),
                ('organizerType', models.TextField()),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='cm_events.EventOrganizer', null=True)),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'cm_events_eventorganizer_translation',
                'db_tablespace': '',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField()),
                ('resource', models.ForeignKey(to='archive.Resource')),
            ],
        ),
        migrations.AddField(
            model_name='eventlink',
            name='link',
            field=models.ForeignKey(to='cm_events.Link'),
        ),
        migrations.AddField(
            model_name='event',
            name='eventOrganizers',
            field=models.ForeignKey(to='cm_events.EventOrganizer'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.OneToOneField(to='locations.Location'),
        ),
        migrations.AlterUniqueTogether(
            name='eventorganizertranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
