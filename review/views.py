from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Project,Profile
from .forms import NewProjectForm
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



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
