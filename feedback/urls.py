from django.urls import path
from . import views

app_name = 'feedback'
urlpatterns = [
    #Показываем проекты в категории
    path('', views.index, name='index'),
]