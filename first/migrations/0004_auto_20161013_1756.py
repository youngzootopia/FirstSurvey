# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_clist_shotinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
