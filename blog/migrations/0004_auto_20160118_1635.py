# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_data_number_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='number_likes',
            field=models.IntegerField(default=0),
        ),
    ]