# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_auto_20161011_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clist',
            fields=[
                ('CID', models.IntegerField(serialize=False, primary_key=True)),
                ('Category', models.CharField(max_length=255, null=True, blank=True)),
                ('ProgramNuame', models.CharField(max_length=255, null=True, blank=True)),
                ('EpisodeNum', models.IntegerField()),
                ('VideoURL', models.CharField(max_length=255, null=True, blank=True)),
                ('VideoFileName', models.CharField(max_length=255, null=True, blank=True)),
                ('VideoThumb', models.CharField(max_length=255, null=True, blank=True)),
                ('FPS', models.FloatField()),
                ('RegisterDateTime', models.DateTimeField()),
                ('LastSavedDateTime', models.DateTimeField()),
                ('TagStatus', models.IntegerField()),
                ('User', models.CharField(max_length=255, null=True, blank=True)),
                ('ProgramNameKor', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShotInfo',
            fields=[
                ('ShotID', models.IntegerField(serialize=False, primary_key=True)),
                ('ShotNum', models.IntegerField()),
                ('StartFrame', models.IntegerField()),
                ('EndFrame', models.IntegerField()),
                ('ThumbURL', models.CharField(max_length=255, null=True, blank=True)),
                ('CID', models.ForeignKey(to='first.Clist')),
            ],
        ),
    ]
