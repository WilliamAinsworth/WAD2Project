# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-18 16:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pubway', '0012_auto_20180314_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcrawl',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(default='default.jpeg', upload_to='profiles'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
