# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20170430_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='level',
            field=models.PositiveIntegerField(db_index=True, default=None, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='lft',
            field=models.PositiveIntegerField(db_index=True, default=None, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='rght',
            field=models.PositiveIntegerField(db_index=True, default=None, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=None, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='category.Category'),
        ),
    ]
