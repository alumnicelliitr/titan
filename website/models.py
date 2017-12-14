# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class NewsLetter(models.Model):
    title = models.CharField(max_length=100, verbose_name='NewsLetter Title')
    content = models.TextField(verbose_name='NewsLetter Content')
    external_link = models.URLField()
    pub_date = models.DateTimeField(verbose_name='Published on')
    image = models.ImageField(upload_to='img/newsletter/', default=None, verbose_name='NewsLetter Image')

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField('Event Details')
    link = models.URLField(verbose_name='External links')
    venue = models.CharField(max_length=100, default=None, blank=True)
    date = models.DateTimeField(verbose_name='Event Date', default=None)

    def __str__(self):
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='image', on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='img/events', default=None, verbose_name='Image')
    description = models.CharField(max_length=50, verbose_name='Small Description of Image', default=None)


class Team(models.Model):
    name = models.CharField(max_length=25, verbose_name='Team name')

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=40)
    contact_no = models.CharField(max_length=15)
    batch_of = models.PositiveIntegerField(default=None)
    branch = models.CharField(max_length=40, default=None)
    role = models.CharField(max_length=20)
    link = models.URLField(verbose_name='Link to Profile')
    team = models.ForeignKey(Team, related_name='member', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mou(models.Model):
    name = models.CharField(max_length=100, verbose_name='University Name')
    country = models.CharField(max_length=20)
    letter = models.FileField(max_length=None, upload_to='mou/', default=None)
    # link = models.URLField(default=None)


class Headlines(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default=None)
    image = models.ImageField(upload_to='img/headlines', default='None')
    link = models.URLField(default=None)


class Publication(models.Model):
    KNOW_YOUR_ALUMNI = 'KYA'
    SHARE_YOUR_STORY = 'SYS'
    TYPES_OF_PUBLICATIONS = (
        (KNOW_YOUR_ALUMNI, 'Know Your Alumni'),
        (SHARE_YOUR_STORY, 'Share Your Story'),
    )

    title = models.CharField(max_length=200)
    type = models.CharField(choices=TYPES_OF_PUBLICATIONS, max_length=3, default=None)
    content = models.TextField()
