# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-30 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiVolontaria', '0003_activationtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationtoken',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation date'),
        ),
    ]
