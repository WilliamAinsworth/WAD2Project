# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-16 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubway', '0015_auto_20180316_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]