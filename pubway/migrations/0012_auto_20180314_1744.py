# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-14 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubway', '0011_auto_20180314_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True),
        ),
    ]
