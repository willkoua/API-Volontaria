# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-30 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiVolontaria', '10000_auto_20180226_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actiontoken',
            name='type',
            field=models.CharField(choices=[('account_activation', 'Account activation'), ('password_change', 'Password change')], default=None, max_length=100, verbose_name='Type of action'),
        ),
    ]
