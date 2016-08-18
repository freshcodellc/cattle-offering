# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-18 05:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0003_auto_20160816_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('caption', models.CharField(max_length=100)),
                ('original_image', models.ImageField(upload_to='cattle_images')),
                ('cattle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='cattle.Cattle')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
