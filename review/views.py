
from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Comment, Project,Profile,NewsLetterRecipients, Ratings
from .forms import NewProjectForm,NewsLetterForm,RatingForm,CommentForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectsSerializer
from review import serializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import serializers
from .permissions import IsAdminOrReadOnly



# @login_required(login_url='/accounts/login/')
def welcome(request):
    profiles=Profile.objects.all()
    project= Project.display_all_projects()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
    else:
            form = NewsLetterForm()

   
    return render(request,'welcome.html',{"project":project,"profiles":profiles,"form":form})


def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)

@login_required(login_url='/accounts/login/')
def display_all_projects(request):
    try:
        project = Project.objects.all()
        print(project)
        return render(request,"project.html", {"projects":project})

    except Project.DoesNotExist:
        raise Http404()
    



@login_required(login_url='/accounts/login/')
def new_projects(request):
  pk = request.GET.get('pk')
  if request.method == 'POST':
    form = NewProjectForm(request.POST, request.FILES)
    if form.is_valid():
      project = form.save(commit=False)
      project.profile = pk
      project.save()
      return redirect('/',{"pk":pk})

  else:
    form = NewProjectForm()
  return render(request, 'new_project.html', {"form": form})


def search_results(request):
    
  if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"project": searched_project})
  
  else:
    message="No search made"
    return render(request,"search.html",{"message":message})

def review_project(request,id):
    project = Project.objects.filter(id=id)
    current_user = request.user

    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.project_id = id
            form.save()
            return redirect('review_project',id)
    else:
        form=CommentForm()

    try:
        user_comment=Comment.objects.filter(project_id=id)
    except Exception as e:
        raise Http404()
   
    return render(request, 'ratings.html',{'project':project, 'current_user': current_user,  'form':form, 'comments':user_comment })

# @login_required
# def rating(request):
#     pk = request.GET.get('pk')
#     try:
#         project = get_object_or_404(Project, pk=id)
#     except:
#         project = None
#         return redirect('index')

#     if request.method == 'POST':
#         form = RatingForm(request.POST)

#         if form.is_valid():
#             rating = form.save(commit=False)
#             project.profile = pk
#             rating.project = project
#             rating.save()
#             return redirect('/')

#     else:
#         form = RatingForm()

#     rating = Ratings.objects.filter(project__pk=id)
#     print(rating)

#     return render(request, 'rating.html', {"rating": rating, "project": project, "form": form})  


@login_required(login_url='/accounts/login/')
def project_profile(request):
    current_user = request.user
    current_user_id=request.user.id
    projects= Project.objects.all()
    
    print(current_user)
   
    
    return render(request, 'profile.html',{"current_user_id":current_user_id, "projects":projects}) 


#start class base api
class ProfileList(APIView):
  permission_classes = (IsAdminOrReadOnly,)  
  def get(self,request,format=None):
    profiles=Profile.objects.all()
    serializers=ProfileSerializer(profiles,many=True)
    return Response(serializers.data)

class ProjectsList(APIView):
  permission_classes = (IsAdminOrReadOnly,)   
  def get(self,request,format=None):
    projects=Project.objects.all()
    serializers=ProjectsSerializer(projects,many=True)
    return Response(serializers.data)