# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 13:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pubway', '0003_auto_20180322_0200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcrawl',
            old_name='firstSt',
            new_name='first_st',
        ),
        migrations.RenameField(
            model_name='subcrawl',
            old_name='loc',
            new_name='sub_cur_loc',
        ),
        migrations.RenameField(
            model_name='subcrawl',
            old_name='name',
            new_name='sub_name',
        ),
        migrations.RenameField(
            model_name='subcrawl',
            old_name='places',
            new_name='sub_places',
        ),
        migrations.RemoveField(
            model_name='subcrawl',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='subcrawl',
            name='organiser',
        ),
        migrations.AddField(
            model_name='subcrawl',
            name='sub_date',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='subcrawl',
            name='sub_organiser',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subcrawl',
            name='sub_slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AddField(
            model_name='subcrawl',
            name='sub_time',
            field=models.TimeField(default='18:00'),
        ),
        migrations.AlterField(
            model_name='subcrawl',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subcrawl',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]