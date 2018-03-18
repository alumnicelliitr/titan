# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-15 18:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0006_donation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=500)),
                ('description', models.TextField(default=None)),
                ('link', models.URLField(verbose_name='Donation Link')),
            ],
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='address_for_correspondence',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='degree_branch',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='degree_name',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='degree_year',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='delivery_address',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='email',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='present_dept',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='present_desig',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='present_office',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='present_residence',
        ),
        migrations.RemoveField(
            model_name='alumnicard',
            name='telephone',
        ),
        migrations.AddField(
            model_name='alumnicard',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='alumniCard', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('GL', 'Guest Lecture'), ('', ''), ('Ruby', 'Ruby Jublee'), ('Meet', 'Alumni meet')], default=None, max_length=20),
        ),
    ]