# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0002_auto_20160902_0249'),
        ('banner', '0003_button'),
    ]

    operations = [
        migrations.AddField(
            model_name='button',
            name='link',
            field=models.ForeignKey(blank=True, help_text='CTA link for this button', null=True, on_delete=django.db.models.deletion.CASCADE, to='link.Link'),
        ),
        migrations.AlterField(
            model_name='button',
            name='text',
            field=models.CharField(help_text='The text to be displayed as the button labal', max_length=60),
        ),
    ]
