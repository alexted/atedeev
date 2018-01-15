from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
####from django.http import Http404

# Create your views here.

####from django.http import HttpResponse
####from django.template import loader

from .models import Elements

#здесь показываем Категории
def index(request):
    latest_elements_list = Elements.objects.order_by('-date_time')[:6]

    context = {
        'latest_elements_list': latest_elements_list,
    }
    return render(request, 'gallery/index.html',context)

#Здесь показываем проекты в зависимости от категории
def detail(request, element_id):
    projects = get_object_or_404(Elements, pk=element_id)
    paginator = Paginator(projects, 6)
    page = request.GET.get('page')
    return render(request, 'gallery/detail.html', {'project': project})

# Здесь показываем конкретный проект
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)