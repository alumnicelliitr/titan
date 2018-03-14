# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from core.models import *
from django.db import models
from django_countries.fields import CountryField
from core.models import User
import os

# TODO: Make a model for Awards

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
    EVENT_TYPES = (
        ("Golden", "Golden Jublee"),
        ("Silver", "Silver Jublee"),
        ("Ruby", "Ruby Jublee"),
        ("Meet", "Alumni meet")
    )
    """
    List of upcoming and complete events with image gallery
    """
    title = models.CharField(max_length=100)
    # type = models.CharField(max_length=20, default="Alumni Meet", verbose_name="Alumni Meet type")
    type = models.CharField(max_length=20, default=None, choices=EVENT_TYPES)
    content = models.TextField('Event Details')
    link = models.URLField(verbose_name='External links')
    venue = models.CharField(max_length=100, default=None, blank=True)
    start_date = models.DateTimeField(verbose_name='Event start Date', default=None)
    end_date = models.DateTimeField(verbose_name='Event end Date', default=None)
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
    link = models.URLField(verbose_name='University Website Link')

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


# two apis for mainpage true
class Headline(models.Model):
    """
    weekly Headlines of happenings in IITR.
    """
    title = models.CharField(max_length=100)
    tagLine = models.CharField(max_length=100, blank=True)
    content = models.TextField(default=None)
    image = models.ImageField(upload_to='img/headlines', default='None')
    link = models.URLField(default=None, blank=True)
    mainPage = models.BooleanField(default=False)

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
    title = models.CharField(max_length=100, verbose_name='Title of the Video repository')
    link = models.URLField(default=None, blank=True, verbose_name='Youtube playlist link')

    def __str__(self):
        return "%s the initiative title" % self.initiative.title


class Video(models.Model):
    title = models.CharField(max_length=50, verbose_name='Video Title')
    mainPage = models.BooleanField(default=False)
    link = models.URLField(default=None, )
    VideoRepository = models.ForeignKey(VideoRepository, related_name='videos', on_delete=models.CASCADE)
    description = models.CharField(max_length=50, verbose_name='Video Description', blank=True)

    def __str__(self):
        return self.title


class KnowYourAlumni(models.Model):
    user = models.ForeignKey(User, default=None, related_name='knowYourAlum', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default=None)
    link = models.URLField(default=None, blank=True, verbose_name='External Link')
    description = models.TextField(default=None)
    thumbnail = models.ImageField(verbose_name='Thumbnail', upload_to='img/KnowYourAlum', default=None) # TODO: make a dynamic folder


class ShareYourStory(models.Model):
    user = models.ForeignKey(User, default=None, related_name='shareYourStory', on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100, default=None, verbose_name='Story Title')
    description = models.TextField(default=None)
    link = models.URLField(default=None, verbose_name='Article Link')
    thumbnail = models.ImageField(verbose_name='Image', upload_to='img/ShareYourStory', default=None) # TODO: make a dynamic folder

class Node(models.Model):
    url_name = models.CharField(max_length=50)  # Would be used for URL
    title = models.CharField(max_length=50)  # Would be used for Display Title
    parent = models.ForeignKey('self', null=True, blank=True, related_name='Parent')
    visibility = models.BooleanField(default=True)
    external_url = models.CharField(max_length=100, null=True, blank=True)
    level = models.IntegerField(default=0)
    content = models.TextField(default='')

    def __str__(self):
        return self.title + " @ " + str(self.level)

    def get_all_children(self, include_self=True):
        r = []
        if include_self:
            r.append(self)
        for c in Node.objects.filter(parent=self):
            _r = c.get_all_children(include_self=True)
            if 0 < len(_r):
                r.extend(_r)
        return r

    class Meta:
        app_label = 'website'


def get_file_path(instance, filename):
    name, ext = os.path.splitext(filename)
    return '{0}/{1}'.format("img/alumnicard", str(instance.first_name) + str(ext))


class AlumniCard(models.Model):
    ADDRESS_CHOICES = (
        ("Office Address", "Office Address"),
        ("Residence Address", "Residence Address")
    )

    DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')
    YEAR_CHOICES = ((x, x) for x in range(1847, 2017))
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    degree_name = models.CharField(max_length=255)
    degree_branch = models.CharField(max_length=255)
    degree_year = models.IntegerField(choices=YEAR_CHOICES)
    present_desig = models.CharField(max_length=255)
    present_dept = models.CharField(max_length=255)
    present_office = models.TextField()
    present_residence = models.TextField()
    delivery_address = models.TextField()
    telephone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    address_for_correspondence = models.CharField(choices=ADDRESS_CHOICES, max_length=50)
    photo = models.ImageField(blank=False, upload_to=get_file_path)
    photo_sign = models.ImageField(blank=False, upload_to=get_file_path)
    photo_degree = models.ImageField(blank=False, upload_to=get_file_path)

    def __str__(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name

    ## add Mail in the front end
