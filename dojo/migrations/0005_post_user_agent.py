# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-07 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0004_auto_20171107_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_agent',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]