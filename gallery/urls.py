from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    #Показываем проекты в категории
    path('category/<slug:category_name>/',views.index, name='index'),
    #Показываем проект
    path('detail/<slug:slug_header>/', views.detail, name='detail'),
]