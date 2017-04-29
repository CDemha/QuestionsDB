# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20170429_0803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='datePosted',
            new_name='date_modified',
        ),
        migrations.AddField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
