
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Project,Profile,NewsLetterRecipients
from .forms import NewProjectForm,NewsLetterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


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
        project= Project.objects.get(id = project_id)
    except Project.DoesNotExist:
        raise Http404()
    return render(request,"project.html", {"project":project})



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

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def project_profile(request):
    current_user = request.user
    current_user_id=request.user.id
    projects= Project.objects.all()
    
    print(current_user)
   
    
    return render(request, 'profile.html',{"current_user_id":current_user_id, "projects":projects}) 