# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 08:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0013_auto_20171123_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='item_id',
        ),
    ]
