# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0011_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='seller_rate',
            field=models.IntegerField(),
        ),
    ]
