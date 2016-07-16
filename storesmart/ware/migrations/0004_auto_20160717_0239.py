# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ware', '0003_auto_20160716_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='cold_rate',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='hot_rate',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='mild_rate',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='severe_rate',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
    ]
