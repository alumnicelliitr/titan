# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-14 20:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20180327_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distinguishedalumninominee',
            name='nominee_optional1',
        ),
    ]
