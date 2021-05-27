from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
  image= CloudinaryField("media")
  title=models.CharField(max_length=200)
  description= models.TextField(max_length=600)
  link= models.CharField(max_length=200)
  
  def __str__(self):
      return self.title
  
  def save_project(self):
        self.save()
      
  def update_description(self):
      self.save()

  def delete_project(self):
      self.delete()

class Profile(models.Model):
  profile_pic =CloudinaryField("profilepics",null= True)
  bio = HTMLField(blank=True)
  name = models.CharField(max_length=255)
  email= models.EmailField(blank=True)
  
  def __str__(self):
      return self.name
  
  def save_profile(self):
        self.save()
      
  def update_profile(self):
      self.save()

  def delete_profile(self):
      self.delete()