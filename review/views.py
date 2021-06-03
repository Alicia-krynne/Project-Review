
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Project,Profile,NewsLetterRecipients, Ratings
from .forms import NewProjectForm,NewsLetterForm,RatingForm
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

def welcome(request):
    profiles=Profile.objects.all()
    project= Project.objects.all()
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

   
    return render(request,'welcome.html',{"project":project,"profiles":profiles,"letterForm":form  },)


def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)

@login_required(login_url='/accounts/login/')
def projects(request,project_id):
    try:
         project = Project.objects.get(id=project_id)

    except Project.DoesNotExist:
        raise Http404()
    return render(request,"project.html", {"project":project , "project_id": project_id})



@login_required(login_url='/accounts/login/')
def new_projects(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.editor = current_user
            project.save()
        return redirect('projects/')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})


def search_results(request):
    
  if "project" in request.GET and request.GET["project"]:
    search=request.GET.get("project")
    rated=False
    try:
      project=Project.search_results(search)
      if len(project)==1:
        single_project=project[0]
        form = RatingForm()
        project_votes=Ratings.project_votes(single_project.id)
        project_voters=single_project
        voters_lists=Ratings.project_voters(single_project.id)
        ratings = Ratings.project_votes(single_project.id)
        voters_list=[i.rater for i in voters_lists]

        for vote in project_votes:
          current_user=request.user
          try:
            user=User.objects.get(pk=current_user.id)
            profile=Profile.objects.get(user=user)
            voters=Ratings.project_voters(profile)
            rated=False
            if current_user.id in voters_list:
              rated=True
          except Profile.DoesNotExist:
            rated=False
        
        project = Project.objects.get(name=search)
        ratings = Ratings.project_votes(project.id)
        rating_stats = ratings.count()
        form = RatingForm()
        current_user = request.user
        profile = Profile.objects.get(user=current_user)
        rating_status = None
        raters = []
        project_average = []
        content_list = []
        design_list = []
        usability_list = []
        for rate in ratings:
          raters.append(rate.rater.id)
          sum_average = rate.usability + rate.design + rate.content
          average = sum_average/3
          project_average.append(average)
          content_list.append(rate.content)
          usability_list.append(rate.usability)
          design_list.append(rate.design)
          try:
            user = User.objects.get(pk=request.user.id)
            profile = Profile.objects.get(user=user)
            rater = Ratings.project_voters(profile)
            rating_status = False
            if request.user.id in raters:
              rating_status = True
          except Profile.DoesNotExist:
            rating_status = False

        average_rating = 0
        design_average = 0
        usability_average = 0
        content_average = 0
        if len(project_average) > 0:
          average_rating = sum(project_average)/len(project_average)
          project.average_rating = round(average_rating, 2)
          project.save()
        if rating_stats != 0:
          usability_average = sum(usability_list)/rating_stats
          content_average = sum(content_list)/rating_stats
          design_average = sum(design_list)/rating_stats
          project.usability_average = round(usability_average, 2)
          project.content_average = round(content_average, 2)
          project.design_average = round(design_average, 2)
          project.save()

        return render(request,'search.html',{"projects":project,"ratings":ratings,"form":form,"project":single_project,"rating_status":rated,"project_votes":project_votes,"project_voters":project_voters,"voters":voters})
      elif len(project) >= 2:
        stats=project.count()
        return render(request,"search.html",{"stats":stats,"project":project})
    
    except Project.DoesNotExist:
      all_projects=Project.get_all_projects()
      message = f"{search} Does not exist"
      return render(request,"search.html",{"message":message,"all_projects":all_projects})

  else:
    message="No search made"
    return render(request,"search.html",{"message":message})

@login_required
def rate_project(request, project_id):
  if request.method == "POST":
    form = RatingForm(request.POST)
    project = Project.objects.get(pk=project_id)
    current_user = request.user
    try:
        user = User.objects.get(pk=current_user.id)
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        raise Http404()
    if form.is_valid():
      ratings = form.save(commit=False)
      ratings.rater = profile
      ratings.projects = project
      ratings.save()
      return HttpResponseRedirect(reverse('project', args=[int(project.id)]))
  else:
      form = RatingForm()
  return render(request, 'project.html', {"form": form})


@login_required(login_url='/accounts/login/')
def project_profile(request):
    current_user = request.user
    current_user_id=request.user.id
    projects= Project.objects.all()
    
    print(current_user)
   
    
    return render(request, 'profile.html',{"current_user_id":current_user_id, "projects":projects}) 

#start class base api
class ProfileList(APIView):
  def get(self,request,format=None):
    profiles=Profile.objects.all()
    serializers=ProfileSerializer(profiles,many=True)
    return Response(serializers.data)

class ProjectsList(APIView):
  def get(self,request,format=None):
    projects=Project.objects.all()
    serializers=ProjectsSerializer(projects,many=True)
    return Response(serializers.data)