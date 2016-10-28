# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('group', models.CharField(max_length=5, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='suser',
            name='phone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
