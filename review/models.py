from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
import cloudinary
from cloudinary.models import CloudinaryField
from django.http import Http404


# Create your models here.
class Project(models.Model):
  image= CloudinaryField("media")
  title=models.CharField(max_length=200)
  description= models.TextField(max_length=600)
  link= models.CharField(max_length=200)
  profile = models.ForeignKey('Profile',models.SET_NULL,null=True)
  
  
  def __str__(self):
      return self.title
  
  def save_project(self):
        self.save()
      
  def update_description(self):
      self.save()

  def delete_project(self):
      self.delete()
  @classmethod
  def get_project(request, id):
        try:
            project = Project.objects.get(pk = id)

        except Project.ObjectDoesNotExist:
            raise Http404()
        
        return project

  @classmethod
  def display_all_projects(cls):
        projects = cls.objects.all()
        return projects

  @classmethod
  def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

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

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


class Ratings(models.Model):
  design = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))),blank=False)
  usability = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))),blank=False)
  content = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))),blank=False)
  rater = models.ForeignKey(Profile,on_delete=models.CASCADE)
  projects=models.ForeignKey(Project,on_delete=models.CASCADE, related_name='ratings')
  design_average=models.FloatField(default=0)
  usability_average=models.FloatField(default=0)
  content_average=models.FloatField(default=0)
  average_rating=models.FloatField(default=0)
  
  def __str__(self):
    return self.projects

  def save_rating(self):
    self.save()
  
  def delete_rating(self):
    self.delete()

  @classmethod
  def project_votes(cls,project):
    return cls.objects.filter(projects=project)

  @classmethod
  def project_voters(cls,rater):
    return cls.objects.filter(rater=rater)
