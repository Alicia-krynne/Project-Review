from django.db import models
from django.db.models import fields
from .models import Profile,Project

from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('id','name','bio','email','profile_pic')

class ProjectsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields=('id','title','description','image','links',)
