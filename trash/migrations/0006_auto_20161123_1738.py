# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0005_auto_20161123_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trashitem',
            name='item_img',
            field=models.CharField(blank=True, default=None, max_length=2058, null=True),
        ),
    ]
