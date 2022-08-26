from typing import final
from django.contrib.admin import options
from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models.base import Model, ModelStateFieldsCacheDescriptor
from django.db.models.deletion import CASCADE
from embed_video.fields import EmbedVideoField 
# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User , on_delete=CASCADE)
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    rate = models.CharField(max_length=10)
    Email_user = models.EmailField()
    photo = models.ImageField(upload_to='profile_pics')
    
class schedule(models.Model):
    name_day =models.CharField(max_length=50)
    day = models.DateField()
    session_num = models.CharField(max_length=20)
    notes = models.CharField(max_length=1000)

class Final(models.Model):
    final = models.DateField()
    
  
class assignment(models.Model):
    ass_name = models.CharField(max_length=50)
    details = models.TextField()
    deadline = models.DateField()
    pdf = models.FileField(upload_to='pdf_ass')
    url_form =models.URLField(max_length=200)



class Uploads(models.Model):
    video = EmbedVideoField() 
    pdf = models.FileField(upload_to='pdf')
    session_title= models.CharField(max_length=50)
