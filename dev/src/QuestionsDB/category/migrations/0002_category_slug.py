# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(auto_created=True, blank=True, null=True),
        ),
    ]
