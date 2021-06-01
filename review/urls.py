from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.welcome,name='Welcome'),
    path('projects/',views.projects,name='projects'),
    path('search/', views.search_results, name='search_results'),
    path('new-projects/', views.new_projects, name='new-project'),
    # path('ajax/newsletter/', views.newsletter, name='newsletter'),
    # path('api/projects/', views.MerchList.as_view()),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)