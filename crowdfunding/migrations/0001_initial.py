from __future__ import unicode_literals

import crowdfunding.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funds', models.PositiveIntegerField()),
                ('alumni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funds', to='core.Alumni', verbose_name='Alumni Name')),
            ],
            options={
                'ordering': ['funds'],
            },
        ),
        migrations.CreateModel(
            name='StudentsProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('timeline', models.FileField(upload_to=crowdfunding.models.get_file_path)),
                ('project_image', models.ImageField(blank=True, null=True, upload_to=crowdfunding.models.get_image_path)),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('alum_votes', models.ManyToManyField(help_text='Alumni who voted for this project', related_name='votedprojects', to='core.Alumni', verbose_name='Votes Alumni')),
                ('students', models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Students')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='fund',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funds', to='crowdfunding.StudentsProject', verbose_name='Project Name'),
        ),
    ]
