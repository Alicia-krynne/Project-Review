from django.contrib import admin
from .models import Comment, Project,Profile,Ratings
# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Ratings)
admin.site.register(Comment)