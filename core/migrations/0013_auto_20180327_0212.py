# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-26 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20180319_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistinguishedAlumniNominator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominator_name', models.CharField(max_length=50)),
                ('nominator_email', models.EmailField(max_length=254)),
                ('nominator_contact', models.CharField(max_length=20)),
                ('nominator_designation', models.CharField(max_length=50)),
                ('nominator_address', models.TextField()),
                ('nominator_affiliation', models.TextField()),
                ('nominator_moreinfo', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DistinguishedAlumniNominee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominee_name', models.CharField(max_length=100)),
                ('nominee_email', models.EmailField(max_length=254)),
                ('nominee_contact', models.CharField(max_length=20)),
                ('nominee_degree', models.CharField(max_length=50)),
                ('nominee_yearpass', models.IntegerField()),
                ('nominee_quals', models.TextField(blank=True, null=True)),
                ('nominee_address', models.TextField()),
                ('nominee_designation', models.CharField(max_length=50)),
                ('nominee_category', models.CharField(choices=[('AR', 'Academic Research'), ('CE', 'Corporate Development/Adminstration/Entrepreneurship'), ('SA', 'Social Sciences/Engineering and Services/Public Adminstration'), ('SS', 'Service to Society')], max_length=100)),
                ('nominee_description', models.TextField()),
                ('nominee_webpage', models.CharField(blank=True, max_length=50, null=True)),
                ('nominee_linkedin', models.CharField(blank=True, max_length=50, null=True)),
                ('nominee_awards', models.TextField(blank=True, null=True)),
                ('nominee_photo', models.ImageField(upload_to='distinguisted/images/')),
                ('nominee_resume', models.FileField(upload_to='distinguisted/resumes/')),
                ('nominee_optional1', models.FileField(blank=True, upload_to='distinguisted/optional/')),
            ],
        ),
        migrations.AddField(
            model_name='distinguishedalumninominator',
            name='nominee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nominator', to='core.DistinguishedAlumniNominee'),
        ),
    ]
