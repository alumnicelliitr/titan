from __future__ import unicode_literals
#from django.urls import reverse 
from django.db import models
from core.models import User

import uuid
import os

# Create your models here.


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)



class Alum_Fund(models.Model):
    first_name = models.CharField(max_length=100,verbose_name="First Name")
    last_name = models.CharField(max_length=100,verbose_name="Last Name")
    funds = models.IntegerField(verbose_name="Funds Given")
    def __str__(self):
        return '%s, %s, %s' % (self.first_name, self.last_name,self.funds)

    class Meta:
        ordering = ["first_name"]
        
class Alum_Votes(models.Model):
    first_name = models.CharField(max_length=100,verbose_name="First Name")
    last_name = models.CharField(max_length=100,verbose_name="Last Name")
    votes = models.IntegerField(verbose_name="Votes Given")

    def __str__(self):
        return '%s, %s, %s' % (self.first_name, self.last_name,self.votes)

    class Meta:
        ordering = ["first_name"]        
        

class Students_Project(models.Model):
    """
    Model representing a Student_project
    """
    title = models.CharField(max_length=200,verbose_name="Title")
    student = models.ManyToManyField(User,verbose_name="Student",related_name="Student User+")
    alumni = models.ManyToManyField(User,verbose_name="Alumni",related_name="Alumni User+")
    votes = models.IntegerField(verbose_name="Votes")
    timeline = models.CharField(max_length=200,verbose_name="Timeline")
    project_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    funds = models.IntegerField(verbose_name="Allocated Amount ")
    raised_amount =  models.IntegerField(verbose_name="Raised Amount")
    description = models.TextField(max_length=1000,verbose_name="Description")
    alum_funds = models.ManyToManyField(Alum_Fund,help_text="Alumni who funded for this project",verbose_name="Funds Alumni")
    alum_votes = models.ManyToManyField(Alum_Votes,help_text="Alumni who voted for this project",verbose_name="Votes Alumni")    

   
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s, %s, %s, %s, %s' % (self.title, self.votes, self.project_image, self.funds, self.votes,self.description)
    
    class Meta:
        ordering = ["title"]    
