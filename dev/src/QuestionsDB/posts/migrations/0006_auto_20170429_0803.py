# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20170428_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug_field',
            field=models.SlugField(auto_created=True, blank=True, null=True),
        ),
    ]
