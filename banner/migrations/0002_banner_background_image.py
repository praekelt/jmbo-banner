# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 12:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jmbo', '0008_auto_20170921_2131'),
        ('banner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='background_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jmbo.Image'),
        ),
    ]