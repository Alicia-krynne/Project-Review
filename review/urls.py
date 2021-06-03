from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.welcome,name='Welcome'),
    path('projects/',views.projects,name='projects'),
    path('search/', views.search_results, name='search_results'),
    path('new/project/', views.new_projects, name='new-project'),
    path('profile/',views.project_profile,name = 'profile'),
    path('ajax/newsletter/', views.newsletter, name='newsletter'),
    re_path('rate_project/(?P<project_id>\d+)',views.rate_project,name = 'rate_project'),
    path('api/profiles/',views.ProfileList.as_view()),
    path('api/projects/',views.ProjectsList.as_view()),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)