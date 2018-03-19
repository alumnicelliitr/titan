# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from datetime import datetime
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import uuid


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

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)



BRANCHES = (
('ACA','Advanced Chemical Analysis'),
('AGPT','Geophysical Technology'),
('AHEC','Alternate Hydro Energy Centre'),
('AHES','Alternate Hydro Energy Systems'),
('AR','Architecture and Planning'),
('ARCD','Architecture Department'),
('ASED','Applied Science and Engineering Department'),
('BE','M.Tech. Bioprocess Engineering'),
('BST','Building Technology'),
('BT','Biotechnology'),
('BTD','Biotechnology Department'),
('BTMS','Biotechnology'),
('CAG','Control & Guidance'),
('CAPPD','Computer Aided Process Plant Design'),
('CCR','CAD,CAM & Robotics'),
('CDM','Disaster Management and Mitigation'),
('CE','Civil Engineering'),
('CED','Civil Engineering Department'),
('CES','Civil Engineering with specialisation in Structures'),
('CH','Chemical Engineering'),
('CHCPP','B.Tech. (Chemical Engineering) with M.Tech. (Computer Aided Process Plant Design)'),
('CHED','Chemical Engineering Department'),
('CHH','B. Tech. (Chemical Engineering) and M. Tech. (Hydrocarbon Engineering)'),
('CHMS','Chemistry'),
('CNT','Centre of Nanotechnology'),
('CRE','Corrosion Engineering'),
('CSAE','Computer Science & Engineering'),
('CSE','Computer Science and Engineering'),
('CSEC','Communication Systems '),
('CSED','Computer Science and Engineering Department'),
('CSI','B. Tech. (Computer Science & Engineering) and M. Tech. (Information Technology)'),
('CT','Centre for Transportation Systems'),
('CYD','Chemistry Department'),
('DMM','Disaster Mitigation and Management'),
('DWRD','Water Resources Development'),
('ECCS','B.Tech (Electronics & Communication) & M.Tech (Communication System)'),
('ECE','Electronics & Communication Engineering'),
('ECED','Electronics and Communication Engineering'),
('ECW','B. Tech. (Electronics & Communication Engineering) and M. Tech. (Wireless Communication)'),
('EDPE','Electric Drives and Power Electronics'),
('EE','Electrical Engineering'),
('EED','Electrical Engineering Department'),
('EEG','Environmental Engineering'),
('EMRL','Environmental Management of Rivers and Lakes'),
('EPE','B. Tech. (Electrical Engineering) and M.Tech. (Power Electronics)'),
('EPH','Engineering Physics'),
('EQD','Earthquake Department'),
('ESD','Earth Sciences Department'),
('GE','Geomatics Engineering'),
('GPT','Geophysical Technology'),
('GT','Geological Technology'),
('GTE','Geotechnical Engineering'),
('GWH','Ground Water Hydrology'),
('HENG','Hydraulics Engineering'),
('HSD','Humanities and Social Sciences Department'),
('HSEM','Hydroelectric System Engineering and Management'),
('HY','Hydrology'),
('HYD','Hydrology Department'),
('IFS','Infrastructure Systems'),
('II','Institute Instrumentation'),
('IN','Production and Industrial Engineering'),
('INM','Industrial Metallurgy'),
('IPA','Industrial Pollution Abatement'),
('ISHM','Industrial Safety and Hazards Management'),
('ISP','Instrumentation and Signal Processing'),
('IT','Information Technology'),
('IWM','Irrigation Water Management'),
('MAD','Mathematics Department'),
('MAR','Architecture and Planning'),
('MBA','Management and Business Administration'),
('MCA','Master of Computer Application'),
('MDE','Machine Design Engineering'),
('ME','Mechanical Engineering'),
('MEC','M.Sc. Economics'),
('MES','Applied Geology'),
('MET','B.Tech. (Mechanical Engineering) and M.Tech. (Thermal Engineering)'),
('MEV','Micro Electronic and VLSI'),
('MGLT','Geological Technology'),
('MGPT','Geophysical Technology'),
('MHY','Hydrology'),
('MIED','Mechanical and Industrial Engineering'), 
('MMED','Metallurgical and Materials Engineering'),
('MMT','Metallurgy Dual'),
('MSAM','Applied Mathematics'),
('MSC','Chemistry'),
('MSCM','M.Sc. Mathematics'),
('MSCPH','Physics'),
('MSD','Management Studies'), 
('MSIM','M.sc Industrial Mathematics and Informatics'),
('MSM','Applied Mathematics'),
('MSP','Physics'),
('MT','Metallurgical & Materials Engineering'),
('MURP','Master of Urban and Rural Planning'),
('NT','Nanotechnology'),
('PEM','B. Tech. (Process Engineering) and M.B.A.'),
('PHD','Physics'),
('PHM','Materials Engineering'),
('PHPD','Photonics'),
('PISE','Production & Industrial Systems Engineering'),
('PKG','Packaging Technology'),
('PP','Pulp & Paper Technology'),
('PPE','Pulp & Paper Engineering'),
('PPED','Polymer and Process Engineering Department'),
('PS','Polymer Science and Technology'),
('PSE','Power System Engineering'),
('PST','Polymer Science and Technology'),
('PTD','Paper Technology Department'),
('RFM','RF and Microwave Engineering'),
('SAC','System and Control'),
('SD','Soil Dynamics'),
('SDV','Semiconductor Design and VLSI Technology'),
('SE','Structural Engineering'),
('SMC','System Modelling and Control'),
('SSEM','Solid State Electronic Materials'),
('STD','Structural Dynamics'),
('SVRA','Seismic Vulnerability & Risk Assessment'),
('SWH','Surface Water Hydrology'),
('TE','Transportation Engineering'),
('TEMI','Thermal Engineering'),
('TPH','Civil Engineering with specialisation in Structures'),
('TSE','Thermal Systems Engineering'),
('WEMI','Welding Engineering'),
('WM','Watershed Management'),
('WRD','Water Resources Development'),
('WRDMD','Water Resources Development and Management'),
)



class User(AbstractBaseUser, PermissionsMixin):
    YEAR_CHOICES = []
    for r in range(1940, (datetime.now().year + 5)):
        YEAR_CHOICES.append((r, r))

    COURSES = (
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('PHD', 'PHD'),
    )

    HOSTELS = (
        ('RB', 'Rajiv Bhawan'),
        ('RJB', 'Rajendra Bhawan'),
        ('RKB', 'Radhakrishna Bhawan'),
        ('KUB', 'Kautley Bhawan'),
        ('RVB', 'Ravindra Bhawan'),
        ('JB', 'Jawahar Bhawan'),
        ('GNB', 'Ganga Bhawan'),
        ('GB', 'Govind Bhawan'),
        ('KB', 'Kasturba Bhawan'),
        ('SB', 'Sarojini Bhawan'),
    )
    name = models.CharField(max_length=50, verbose_name="Name")
    email = models.EmailField(max_length=255, null=True, unique=True, verbose_name='Official Email Address')
    email_1 = models.EmailField(max_length=255, unique=True, verbose_name='Unofficial Email Address', blank=True, null=True)
    enr_no = models.IntegerField(primary_key=True, verbose_name='Enrollment Number')
    image = models.ImageField(upload_to='users', blank=True, null=True)
    dob = models.DateField(null=True, blank=True, verbose_name='Date Of Birth')
    joining_date = models.DateField(null=True, blank=True, verbose_name='Date Of Joining')
    leaving_date = models.DateField(null=True, blank=True, verbose_name='Date Of Leaving')
    branch = models.CharField(max_length=7, choices=BRANCHES, verbose_name="Branch")
    course = models.CharField(max_length=7, choices=COURSES, verbose_name="Course")
    hostel = models.CharField(max_length=3, choices=HOSTELS, verbose_name="Hostel", null=True, blank=True)
    room_no = models.CharField(max_length=6, null=True, blank=True)
    gender = models.CharField(null=True, blank=True, max_length=1, choices=(('F', 'Female'), ('M', 'Male')), verbose_name="gender")
    degree = models.FileField(upload_to='degrees', blank=True, null=True)
    aadhar_no = models.BigIntegerField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        verbose_name='Staff Status',
        default=False,
        help_text='Designates whether the user can log into admin site.',
    )

    REQUIRED_FIELDS = ['name', 'email', 'branch', 'course']

    USERNAME_FIELD = 'enr_no'

    objects = UserManager()

    def get_short_name(self):
        return self.name

    def get_username(self):
        return str(self.enr_no)    

    def __str__(self):
        return str(self.enr_no)

    def __unicode__(self):
        return str(self.enr_no)


class Alumni(models.Model):
    user = models.OneToOneField(User, related_name='alum', verbose_name="Alumni", on_delete=models.CASCADE,
                                primary_key=True)
    alumni_card = models.BooleanField(default="false", verbose_name="Alumni Card")
    is_verified = models.BooleanField(default=False)
    sign = models.ImageField(upload_to='alum_sign', blank=True, null=True, verbose_name='Signature')
    short_bio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '%s' % self.user.name

    class Meta:
        ordering = ["user"]


class Team(models.Model):
    TYPES = (
        ('C', 'Current'),
        ('P', 'Passed'),
        ('F', 'Founding'),
    )
    user = models.OneToOneField(User, related_name='team', verbose_name="Team member", on_delete=models.CASCADE,
                                primary_key=True)
    member_type = models.CharField(max_length=10, choices=TYPES, verbose_name="Member Type")
    role = models.CharField(max_length=20)
    short_bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.user.name

    class Meta:
        ordering = ["user"]        


class Contact(models.Model):
    TYPES = (
        ('Mob', 'Mobile No.'),
        ('Email', 'Email'),
    )
    contact_type = models.CharField(max_length=10, choices=TYPES, verbose_name="Contact Type")
    user = models.ForeignKey(User, verbose_name="User",related_name='contacts', on_delete=models.CASCADE)
    value = models.TextField()
    def __str__(self):
        return str(self.contact_type)

    class Meta:
        verbose_name_plural = "Contacts"
        ordering = ["user"]

class Social(models.Model):
    TYPES = (
        ('FB', 'Facebook'),
        ('TW', 'Twitter'),
        ('IN', 'Instagram'),
        ('SC', 'Snap Chat'),
        ('LI', 'Linked In'),
        ('GH', 'Github'),
    )
    social_type = models.CharField(max_length=10, choices=TYPES, verbose_name="Contact Type")
    user = models.ForeignKey(User, verbose_name="User",related_name='socials', on_delete=models.CASCADE)
    value = models.URLField()

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name_plural = "Social Accounts"


class Skill(models.Model):
    users = models.ManyToManyField(User, related_name='skills', blank=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % self.name


class Location(models.Model):
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    pin = models.IntegerField()
    def __str__(self):
        return '%s' % self.city


class UserLocation(models.Model):
    user = models.ForeignKey(User,related_name='locations', on_delete=models.CASCADE)   
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.user.name + ' '+ self.location.city 

    class Meta:
        ordering = ["user"]        


class Organisation(models.Model):
    TYPES = (
        ('UN', 'University'),
        ('CG', 'Campus Group'),
        ('C', 'Company'),
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    org_type = models.CharField(max_length=10, choices=TYPES, verbose_name="Organisation Type")  
    name  = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.name


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiences')
    org = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='experiences')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  
    description = models.TextField()

    def __str__(self):
        return '%s' % self.user.name + ' '+ self.org.name

    class Meta:
        ordering = ["user"]


class Subscriber(models.Model):
    user = models.OneToOneField(User, related_name='subscriber', verbose_name="Subscriber", on_delete=models.CASCADE,
                                primary_key=True)
    is_subscribed = models.BooleanField(default=True)
    subscription_key = models.CharField(max_length=32,unique=True, blank=True)



from django.core.validators import validate_email
class Visitor(models.Model):
    email = models.EmailField(unique=True,validators=[validate_email])
    is_subscribed = models.BooleanField(default=True)
    subscription_key = models.CharField(max_length=32,unique=True, blank=True)


@receiver(post_save, sender=User)
def create_user_subscriber(sender, instance, created, **kwargs):
    if created:
        Subscriber.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_subscriber(sender, instance, **kwargs):
    instance.subscriber.save()


@receiver(pre_save, sender=Subscriber)
def create_subscriber(sender, instance, **kwargs):
    if instance._state.adding :
      key = uuid.uuid1().hex
      instance.subscription_key = key    

@receiver(pre_save, sender=Visitor)
def create_visitor(sender, instance, **kwargs):
    if instance._state.adding :
      key = uuid.uuid1().hex
      instance.subscription_key = key    



class EmailMessage(models.Model):
  subject = models.CharField(max_length=255)
  created_on = models.DateTimeField(auto_now_add=True)
  message = RichTextField(default='')
  include_name= models.BooleanField(default=True)