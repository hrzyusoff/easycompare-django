# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=200)),
                ('pic', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameModel(
            old_name='page_crawl',
            new_name='PageCrawl',
        ),
        migrations.DeleteModel(
            name='search_item',
        ),
    ]
