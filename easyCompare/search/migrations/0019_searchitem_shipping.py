# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0018_auto_20171127_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchitem',
            name='shipping',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
