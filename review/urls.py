from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.welcome,name='Welcome'),
    path('projects/',views.display_all_projects,name='projects'),
    path('search/', views.search_results, name='search_results'),
    path('new/project/', views.new_projects, name='new-project'),
    path('profile/',views.project_profile,name = 'profile'),
    path('ajax/newsletter/', views.newsletter, name='newsletter'),
    #path('rating/(?P<project_id>\d+)$', views.rating, name = 'rating'),
    path('review_project/?<project_id>', views.review_project, name = 'review_project'),
    path('api/profiles/',views.ProfileList.as_view()),
    path('api/projects/',views.ProjectsList.as_view()),
    # path('rating/(?P<project_id>)', views.rating, name = 'rating'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)