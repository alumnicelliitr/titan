from __future__ import unicode_literals
from django.db import models
from core.models import User,UnivAlum

import uuid
import os

# Create your models here.


def get_image_path(instance, filename):
    name, ext = os.path.splitext(filename)
    return '{0}/{1}'.format("projectimages", str(instance.title)+str(ext))


def get_file_path(instance, filename):
    name, ext = os.path.splitext(filename)
    return '{0}/{1}'.format("projecttimeline", str(instance.title)+str(ext))


class AlumFund(models.Model):
    name = models.CharField(max_length=100,verbose_name="Alumni Name")
    funds = models.IntegerField(verbose_name="Funds Given")
    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        ordering = ["name"]
        


class StudentsProject(models.Model):
    """
    Model representing a Student_project
    """
    title = models.CharField(max_length=200,verbose_name="Title")
    student = models.ManyToManyField(User,verbose_name="Student",related_name="StudentUser+",null=True, blank=True)
    alumni = models.ForeignKey(User,verbose_name="Alumni",related_name="AlumniUser+",null=True, blank=True)
    timeline = models.FileField(upload_to=get_file_path)
    project_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    funds = models.IntegerField(verbose_name="Allocated Amount ")
    description = models.TextField(max_length=1000,verbose_name="Description")
    alum_funds = models.ManyToManyField(AlumFund,help_text="Alumni who funded for this project",verbose_name="Funds Alumni",related_name="AlumFund",null=True, blank=True)
    alum_votes = models.ManyToManyField(User,help_text="Alumni who voted for this project",verbose_name="Votes Alumni",related_name="AlumVote+",null=True, blank=True)    

   
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.title)
    
    class Meta:
        ordering = ["title"]    
