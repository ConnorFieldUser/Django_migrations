# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_creater', '0003_auto_20161004_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='str_accuracy',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='td_accuracy',
            field=models.CharField(max_length=15),
        ),
    ]