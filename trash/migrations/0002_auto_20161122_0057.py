# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrashGeoLoc',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=2058)),
            ],
        ),
        migrations.AddField(
            model_name='trashitem',
            name='item_img',
            field=models.CharField(default=None, max_length=2058),
        ),
        migrations.AddField(
            model_name='trashitem',
            name='sc_code',
            field=models.CharField(default=None, max_length=2058),
        ),
        migrations.AddField(
            model_name='trashbin',
            name='trash_loc',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='trash.TrashGeoLoc'),
        ),
    ]
