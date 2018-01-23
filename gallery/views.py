from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
####from django.http import Http404

# Create your views here.

####from django.http import HttpResponse
####from django.template import loader

from .models import Elements

#здесь показываем Категории
def index(request, category_name):
    projects_list = Elements.objects.filter(category=category_name).order_by('-date_time')[:6]
 #   context = {
 #       'projects_list': projects_list,
 #   }
    page = request.GET.get('page', 1)
    paginator = Paginator(projects_list, 3)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    return render(request, 'gallery/index.html', {'projects' : projects})

#Здесь показываем проекты в зависимости от категории
def detail(request, slug_header):
    project = get_object_or_404(Elements, slug_header = slug_header)
    return render(request, 'gallery/detail.html', {'project': project})

# Здесь показываем конкретный проект
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)