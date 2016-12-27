# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePreview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('LargeImagePreviewLink', models.URLField()),
                ('MediumImagePreviewLink', models.URLField()),
                ('thumbnailImagePreviewLink', models.URLField()),
                ('cachedImagePreview', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resourceLink', models.URLField()),
                ('source', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ResourceImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preview', models.ForeignKey(to='archive.ImagePreview')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceLiveStream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('streamLink', models.URLField()),
                ('cachedStream', models.FileField(upload_to=b'')),
                ('preview', models.ForeignKey(to='archive.ImagePreview')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('VideoLink', models.URLField()),
                ('cachedVideo', models.FileField(upload_to=b'')),
                ('preview', models.ForeignKey(to='archive.ImagePreview')),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='images',
            field=models.ForeignKey(to='archive.ResourceImage'),
        ),
        migrations.AddField(
            model_name='resource',
            name='preview',
            field=models.ForeignKey(to='archive.ImagePreview'),
        ),
        migrations.AddField(
            model_name='resource',
            name='streams',
            field=models.ForeignKey(to='archive.ResourceLiveStream'),
        ),
        migrations.AddField(
            model_name='resource',
            name='videos',
            field=models.ForeignKey(to='archive.ResourceVideo'),
        ),
    ]
