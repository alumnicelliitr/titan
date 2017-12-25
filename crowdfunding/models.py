from __future__ import unicode_literals
from django.db import models
from core.models import Alum,Student

import uuid
import os

# Create your models here.


def get_image_path(instance, filename):
    name, ext = os.path.splitext(filename)
    return '{0}/{1}'.format("projectimages", str(instance.title)+str(ext))


def get_file_path(instance, filename):
    name, ext = os.path.splitext(filename)
    return '{0}/{1}'.format("projecttimeline", str(instance.title)+str(ext))



class StudentsProject(models.Model):
    """
    Model representing a Student_project
    """
    title = models.CharField(max_length=200,verbose_name="Title")
    students = models.ManyToManyField(Student,verbose_name="Students",related_name="projects")
    timeline = models.FileField(upload_to=get_file_path)
    project_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    description = models.TextField(max_length=1000,verbose_name="Description")
    alum_votes = models.ManyToManyField(Alum,help_text="Alumni who voted for this project",verbose_name="Votes Alumni",related_name="votedprojects")    
    
   
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.title)
    
    class Meta:
        ordering = ["title"]    


class Fund(models.Model):
    funds = models.IntegerField()
    project = models.ForeignKey(StudentsProject,related_name="Funds",verbose_name="Project Name")
    alumni = models.ForeignKey(Alum,related_name="Funds",verbose_name="Alumni Name")    
    
    def __str__(self):
        return '%s' % (self.funds)

    class Meta:
        ordering = ["funds"]   
        
        

