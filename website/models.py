# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField
from core.models import User
from django.db.models.fields.related import (
    OneToOneField,
)


class NewsLetter(models.Model):
    """
    models for newsletters to be published on website, they are some important events happening in the campus !
    """
    title = models.CharField(max_length=100, verbose_name='NewsLetter Title')
    content = models.TextField(verbose_name='NewsLetter Content')
    external_link = models.URLField()
    pub_date = models.DateTimeField(verbose_name='Published on')
    image = models.ImageField(upload_to='img/newsletter/', default=None, verbose_name='NewsLetter Image')

    def __str__(self):
        return self.title


class Event(models.Model):
    """
    List of upcoming and complete events with image gallery
    """
    title = models.CharField(max_length=100)
    content = models.TextField('Event Details')
    link = models.URLField(verbose_name='External links')
    venue = models.CharField(max_length=100, default=None, blank=True)
    date = models.DateTimeField(verbose_name='Event Date', default=None)
    coverImage = models.ImageField(verbose_name='Cover Image of Event', upload_to='img/events', default=None)

    def __str__(self):
        return self.title


# creating a dynamic image upload path
def event_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/img/events/event_<id>/<filename>
    return 'img/events/event_{0}/{1}'.format(instance.event.id, filename)


class EventImage(models.Model):
    """
    gallery of the event with small image description for each image
    """
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    pic = models.ImageField(upload_to=event_image_directory_path, default=None, verbose_name='Image')
    description = models.CharField(max_length=50, verbose_name='Small Description of Image', blank=True)


class Team(models.Model):
    """
    various teams of IARC.
    """
    name = models.CharField(max_length=25, verbose_name='Team name')

    def __str__(self):
        return self.name


class Member(models.Model):
    """
    Members of each team and their details
    """
    name = models.CharField(max_length=40)
    contact_no = models.CharField(max_length=15)
    batch_of = models.PositiveIntegerField(default=None)
    branch = models.CharField(max_length=40, default=None)
    role = models.CharField(max_length=20)
    link = models.URLField(verbose_name='Link to Profile')
    team = models.ForeignKey(Team, related_name='members', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mou(models.Model):
    """
    Memorandum of Understanding with another universities in different countries
    """
    name = models.CharField(max_length=100, verbose_name='University Name')
    country = CountryField(blank_label='(select country)')
    letter = models.FileField(max_length=None, upload_to='mou/', default=None)

    # link = models.URLField(default=None)

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    Different courses offered by an University under MoU
    """
    course = models.CharField(max_length=60, verbose_name='Course Name')
    duration = models.CharField(max_length=50, verbose_name='Course Duration')
    mou = models.ForeignKey(Mou, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.course


class Headline(models.Model):
    """
    weekly Headlines of happenings in IITR.
    """
    title = models.CharField(max_length=100)
    content = models.TextField(default=None)
    image = models.ImageField(upload_to='img/headlines', default='None')
    link = models.URLField(default=None, blank=True)

    def __str__(self):
        return self.title


class Initiative(models.Model):
    """
    various initiatives of IARC.
    """
    title = models.CharField(max_length=200, default=None)
    description = models.TextField(verbose_name="Small Description of Initiative", default=None)

    def __str__(self):
        return self.title


def initiative_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/img/events/event_<id>/<filename>
    return 'img/initiatives/initiative_{0}/{1}'.format(instance.initiative.id, filename)


class VideoRepository(models.Model):
    """
    The Video Repository Initiative it can contain one or more videos
    """
    image = models.ImageField(upload_to=initiative_image_directory_path, default=None)

    def __str__(self):
        return "%s the initiative title" % self.initiative.title


class Video(models.Model):
    title = models.CharField(max_length=50, verbose_name='Video Title')
    VideoRepository = models.ForeignKey(VideoRepository, related_name='videos', on_delete=models.CASCADE)
    description = models.CharField(max_length=50, verbose_name='Video Description', blank=True)

    def __str__(self):
        return self.title


class Publication(models.Model):
    KNOW_YOUR_ALUMNI = 'KYA'
    SHARE_YOUR_STORY = 'SYS'
    TYPES_OF_PUBLICATIONS = (
        (KNOW_YOUR_ALUMNI, 'Know Your Alumni'),
        (SHARE_YOUR_STORY, 'Share Your Story'),
    )
    type = models.CharField(choices=TYPES_OF_PUBLICATIONS, max_length=3, default=None)
    link = models.URLField(default=None, verbose_name='External Link')

    def __str__(self):
        return "%s the initiative title" % self.initiative.title


class KnowYourAlumni(models.Model):
    user = models.ForeignKey(User, related_name='', on_delete=models.CASCADE)
    link = models.URLField(default=None, blank=True, verbose_name='External Link')
    description = models.TextField(default=None)


class ShareYourStory(models.Model):
    # user = models.ForeignKey(User, related_name='', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default=None, verbose_name='Story Title')
    description = models.TextField(default=None)
