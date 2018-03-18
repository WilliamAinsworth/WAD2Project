# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-16 16:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubway', '0014_auto_20180316_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='place_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='image',
            name='uploaded_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]