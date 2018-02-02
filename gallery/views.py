from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from .models import Project

#здесь показываем Категории
def index(request, category_name):
    projects_list = Project.objects.filter(category=category_name).order_by('-date_time')[:6]
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
    project = get_object_or_404(Project, slug_header = slug_header)
    return render(request, 'gallery/detail.html', {'project': project})