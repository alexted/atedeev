from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    #Показываем категории
    path('category/<slug:category_name>/',views.index, name='index'),
    #Показываем проекты в категории
    path('detail/<slug:slug_header>/', views.detail, name='detail'),
    #Показываем конкретный проект
    path('<int:element_id>/results/', views.results, name='results'),
    path('<int:element_id>/vote/', views.vote, name='vote'),
]