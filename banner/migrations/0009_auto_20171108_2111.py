# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0008_auto_20171030_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='background_image',
        ),
    ]
