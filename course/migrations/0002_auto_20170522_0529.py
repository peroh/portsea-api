# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 05:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0002_remove_awardcategory_members'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='award_category',
        ),
        migrations.AddField(
            model_name='course',
            name='award_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='award.AwardCategory'),
            preserve_default=False,
        ),
    ]
