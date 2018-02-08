from django.contrib import admin
from .forms import SendMassEmail
from django.shortcuts import render

from .models import Feedback
# Register your models here.

def send_emails_admin_action(modeladmin, request, queryset):
    form = SendMassEmail(initial={'receivers': queryset})
    return render(request, 'feedback/send_emails.html', {'form':form})
send_emails_admin_action.short_description = "Отправить письмо"

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'datetime', 'email')
    list_filter = ['datetime']
    search_fields = ['name', 'message', 'organization']
    actions = [send_emails_admin_action]

admin.site.register(Feedback, FeedbackAdmin)