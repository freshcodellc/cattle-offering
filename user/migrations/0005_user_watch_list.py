# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0002_auto_20160810_2319'),
        ('user', '0004_auto_20160809_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watch_list',
            field=models.ManyToManyField(related_name='watchers', to='cattle.Cattle'),
        ),
    ]