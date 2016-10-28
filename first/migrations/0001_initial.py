# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='SUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('sUserID', models.CharField(max_length=50, unique=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('group', models.CharField(max_length=5, null=True, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('sex', models.CharField(max_length=5, null=True, blank=True)),
                ('married', models.CharField(max_length=5, null=True, blank=True)),
                ('children', models.CharField(max_length=5, null=True, blank=True)),
                ('job', models.CharField(max_length=128, null=True, blank=True)),
                ('company', models.CharField(max_length=128, null=True, blank=True)),
                ('hobby', models.CharField(max_length=128, null=True, blank=True)),
                ('currentShot', models.IntegerField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cID', models.IntegerField()),
                ('shotID', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('fileName', models.CharField(max_length=256)),
                ('preference', models.FloatField()),
                ('reason', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Filtering',
            fields=[
                ('sUserID', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('serviceProvider', models.CharField(max_length=128)),
                ('degree', models.CharField(max_length=64)),
                ('price', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='survey',
            name='sUserID',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='suser',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='suser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='survey',
            unique_together=set([('sUserID', 'shotID')]),
        ),
    ]
