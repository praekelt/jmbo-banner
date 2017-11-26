# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import simplemde.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jmbo', '0007_auto_20170314_1546'),
        ('link', '0002_auto_20160902_0249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('modelbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='jmbo.ModelBase')),
                ('style', models.CharField(choices=[], max_length=128)),
                ('headline', simplemde.fields.SimpleMDEField(blank=True, help_text="The banner's headline.", null=True)),
                ('body', simplemde.fields.SimpleMDEField(blank=True, help_text="The banner's main text content.", null=True)),
                ('link', models.ForeignKey(blank=True, help_text='Link to which this banner should redirect.', null=True, on_delete=django.db.models.deletion.CASCADE, to='link.Link')),
            ],
            bases=('jmbo.modelbase',),
        ),
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='The text to be displayed as the button label', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ButtonOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(default=0)),
                ('banner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banner.Banner')),
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banner.Button')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.AddField(
            model_name='button',
            name='banner',
            field=models.ManyToManyField(blank=True, null=True, related_name='buttons', through='banner.ButtonOrder', to='banner.Banner'),
        ),
        migrations.AddField(
            model_name='button',
            name='link',
            field=models.ForeignKey(blank=True, help_text='CTA link for this button', null=True, on_delete=django.db.models.deletion.CASCADE, to='link.Link'),
        ),
    ]
