from django.contrib import admin
from .forms import SendEmailForm
from django.shortcuts import render
from django.conf import settings

from .models import Feedback
# Register your models here.

def send_email_admin_action(modeladmin, request, queryset):
    form = SendEmailForm(initial={'recipients': queryset, 'sender': settings.DEFAULT_FROM_EMAIL})
    return render(request, 'feedback/send_emails.html', {'form':form})
send_email_admin_action.short_description = "Отправить письмо"

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'datetime', 'email')
    list_filter = ['datetime']
    search_fields = ['name', 'message', 'organization']
    actions = [send_email_admin_action]

admin.site.register(Feedback, FeedbackAdmin)