# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='instru',
            name='endtime',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='instru',
            name='starttime',
            field=models.TimeField(blank=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]