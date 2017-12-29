# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
import datetime

from django_countries.fields import CountryField


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Enter email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        # noinspection PyUnresolvedReferences
        user.set_password(password)
        user.save()
        return user


class TempUser(models.Model):
    YEAR_CHOICES = []
    for r in range(1940, (datetime.datetime.now().year + 5)):
        YEAR_CHOICES.append((r, r))

    name = models.CharField(max_length=50, verbose_name="Name")
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email Address')
    enr_no = models.IntegerField(primary_key=True, verbose_name='Enrollment Number')
    batch = models.IntegerField(choices=YEAR_CHOICES, verbose_name='Batch')
    degree_photo = models.ImageField(upload_to='degree_photo', blank=True, null=True)
    verified = models.BooleanField(default="false")


class CampusGroup(models.Model):
    GROUPS = (
        ('SDS', 'SDSLabs'),
        ('MDG', 'Mobile Development Group'),
        ('IARC', 'IARC'),
        ('GG', 'Geek Gazette'),
        ('WONA', 'Watch Out News Agency')
    )

    group = models.CharField(max_length=4, choices=GROUPS, verbose_name="Group")

    def __str__(self):
        return self.get_group_display()


class User(models.Model):
    YEAR_CHOICES = []
    for r in range(1940, (datetime.datetime.now().year + 5)):
        YEAR_CHOICES.append((r, r))

    BRANCHES = (
        ('BT', 'Biotechnology'),
        ('AR', 'Architecture and Planning'),
        ('CH', 'Chemical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('CSE', 'Computer Science and Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('IN', 'Production and Industrial'),
        ('MT', 'Metallurgical and Materials Engineering'),
        ('PP', 'Pulp and Paper Engineering'),
        ('PS', 'Polymer and Process Engineering'),
        ('EPH', 'Engineering Physics'),
        ('MSM', 'Applied Mathematics'),
        ('GT', 'Geological Technology'),
        ('GPT', 'Geophysical Technology'),
        ('PHD', 'PHD'),
        ('PBT', 'PHD Biotechnology'),
    )

    name = models.CharField(max_length=50, verbose_name="Name")
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email Address')
    enr_no = models.IntegerField(primary_key=True, verbose_name='Enrollment Number')
    image = models.ImageField(upload_to='users', blank=True, null=True)
    dob = models.DateTimeField(verbose_name='Date Of Birth')
    batch = models.IntegerField(choices=YEAR_CHOICES, verbose_name='Batch')
    branch = models.CharField(max_length=3, choices=BRANCHES, verbose_name="Branch")
    interest = models.TextField(max_length=250, verbose_name="Interest")
    campus_groups = models.ManyToManyField(CampusGroup, related_name='users')

    objects = UserManager()

    def __str__(self):
        return str(self.name)


class University(models.Model):
    univ = models.TextField(max_length=25, verbose_name="Universities")

    def __str__(self):
        return str(self.univ)


class Company(models.Model):
    name = models.CharField(max_length=25, verbose_name="Company Name")

    def __str__(self):
        return str(self.name)


class Location(models.Model):
    state = models.CharField(max_length=20, verbose_name="State")
    country = CountryField(blank_label='(select country)')

    def __str__(self):
        return str(self.state + "," + self.country)


class Alum(models.Model):
    user = models.OneToOneField(User, related_name='alum', verbose_name="Alumni", on_delete=models.CASCADE,
                                primary_key=True)
    alumni_card = models.BooleanField(default="false", verbose_name="Alumni Card")
    universities = models.ManyToManyField(University, through='UnivAlum', related_name='alums')
    companies = models.ManyToManyField(Company, through='CompAlum', related_name='alums')
    locations = models.ManyToManyField(Location, related_name='alums')

    def __str__(self):
        return '%s' % self.user.name

    class Meta:
        ordering = ["user"]


class Student(models.Model):
    user = models.OneToOneField(User, related_name='student', verbose_name="Student", on_delete=models.CASCADE,
                                primary_key=True)

    def __str__(self):
        return '%s' % self.user.name

    class Meta:
        ordering = ["user"]


class UnivAlum(models.Model):
    user = models.ForeignKey(Alum, on_delete=models.CASCADE)
    univ = models.ForeignKey(University, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_left = models.DateField()


class CompAlum(models.Model):
    user = models.ForeignKey(Alum, on_delete=models.CASCADE)
    comp = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_left = models.DateField()
