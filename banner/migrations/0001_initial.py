# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-10 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import simplemde.fields
import sortedm2m.fields

from banner.styles import BANNER_STYLE_CLASSES


# Silence new migrations for styles choices alterations
def styles():
    return [
        (klass.__name__, klass.__name__)
        for klass in BANNER_STYLE_CLASSES
    ]


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
                ('style', models.CharField(choices=styles(), default=b'BaseStyle', max_length=128)),
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
                ('banner', sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, null=True, related_name='buttons', to='banner.Banner')),
                ('link', models.ForeignKey(blank=True, help_text='CTA link for this button', null=True, on_delete=django.db.models.deletion.CASCADE, to='link.Link')),
            ],
        ),
    ]
