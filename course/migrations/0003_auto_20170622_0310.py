# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('course', '0002_auto_20170522_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='attendees',
            field=models.ManyToManyField(to='member.Member'),
        ),
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
