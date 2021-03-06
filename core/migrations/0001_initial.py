from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Official Email Address')),
                ('email_1', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Unofficial Email Address')),
                ('enr_no', models.IntegerField(primary_key=True, serialize=False, verbose_name='Enrollment Number')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users')),
                ('dob', models.DateTimeField(blank=True, null=True, verbose_name='Date Of Birth')),
                ('joining_date', models.DateTimeField(blank=True, null=True, verbose_name='Date Of Joining')),
                ('leaving_date', models.DateTimeField(blank=True, null=True, verbose_name='Date Of Leaving')),
                ('branch', models.CharField(choices=[('BT', 'Biotechnology'), ('AR', 'Architecture and Planning'), ('CH', 'Chemical Engineering'), ('CE', 'Civil Engineering'), ('EE', 'Electrical Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('CSE', 'Computer Science and Engineering'), ('ME', 'Mechanical Engineering'), ('IN', 'Production and Industrial'), ('MT', 'Metallurgical and Materials Engineering'), ('PP', 'Pulp and Paper Engineering'), ('PS', 'Polymer and Process Engineering'), ('EPH', 'Engineering Physics'), ('MSM', 'Applied Mathematics'), ('GT', 'Geological Technology'), ('GPT', 'Geophysical Technology')], max_length=3, verbose_name='Branch')),
                ('course', models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('PHD', 'PHD')], max_length=5, verbose_name='Course')),
                ('hostel', models.CharField(blank=True, choices=[('RB', 'Rajiv Bhawan'), ('RJB', 'Rajendra Bhawan'), ('RKB', 'Radhakrishna Bhawan'), ('KUB', 'Kautley Bhawan'), ('RVB', 'Ravindra Bhawan'), ('JB', 'Jawahar Bhawan'), ('GNB', 'Ganga Bhawan'), ('GB', 'Govind Bhawan'), ('KB', 'Kasturba Bhawan'), ('SB', 'Sarojini Bhawan')], max_length=3, null=True, verbose_name='Hostel')),
                ('room_no', models.CharField(blank=True, max_length=6, null=True)),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=1, null=True, verbose_name='gender')),
                ('degree', models.FileField(blank=True, null=True, upload_to='degrees')),
                ('aadhar_no', models.BigIntegerField(blank=True, null=True)),
                ('is_alumni', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into admin site.', verbose_name='Staff Status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(choices=[('Mob', 'Mobile No.'), ('Email', 'Email')], max_length=10, verbose_name='Contact Type')),
                ('value', models.TextField()),
            ],
            options={
                'ordering': ['user'],
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('pin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_type', models.CharField(choices=[('UN', 'University'), ('CG', 'Campus Group'), ('C', 'Company')], max_length=10, verbose_name='Organisation Type')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('url', models.URLField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_type', models.CharField(choices=[('FB', 'Facebook'), ('TW', 'Twitter'), ('IN', 'Instagram'), ('SC', 'Snap Chat'), ('LI', 'Linked In'), ('GH', 'Github')], max_length=10, verbose_name='Contact Type')),
                ('value', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Social Accounts',
            },
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='alum', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Alumni')),
                ('alumni_card', models.BooleanField(default='false', verbose_name='Alumni Card')),
                ('is_verified', models.BooleanField(default=False)),
                ('sign', models.ImageField(blank=True, null=True, upload_to='alum_sign', verbose_name='Signature')),
                ('short_bio', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='team', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Team member')),
                ('member_type', models.CharField(choices=[('C', 'Current'), ('P', 'Passed')], max_length=10, verbose_name='Member Type')),
                ('role', models.CharField(max_length=20)),
                ('short_bio', models.TextField()),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.AddField(
            model_name='userlocation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='social',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='skill',
            name='users',
            field=models.ManyToManyField(related_name='skills', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experience',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='core.Organisation'),
        ),
        migrations.AddField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
