from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Project,Profile
from .forms import NewsLetterForm,NewArticleForm
import datetime as dt
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required(login_url='/accounts/login/')
def projects(request,project_id):
    try:
        project= Project.objects.get(id = project_id)
    except Project.DoesNotExist:
        raise Http404()
    return render(request,"/project.html", {"project":project})




def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
