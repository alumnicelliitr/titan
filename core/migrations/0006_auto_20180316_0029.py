# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-15 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_user_is_alumni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='member_type',
            field=models.CharField(choices=[('C', 'Current'), ('P', 'Passed'), ('F', 'Founding')], max_length=10, verbose_name='Member Type'),
        ),
    ]
