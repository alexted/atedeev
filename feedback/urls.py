from django.urls import path
from . import views

app_name = 'feedback'
urlpatterns = [
    #Показываем проекты в категории
    path('', views.index, name='index'),
    path('send_emails/', views.SendUserEmails.as_view(), name='send_emails')
]