from django.contrib import admin
from .forms import SendMassEmail
from django.shortcuts import render

from .models import Feedback
# Register your models here.

def send_emails(modeladmin, request, queryset):
    form = SendMassEmail(initial={'emails':queryset })
    return render(request, 'feedback/send_emails.html', {'form':form})
send_emails.short_description = "Отправить письмо"

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'datetime', 'email')
    list_filter = ['datetime']
    search_fields = ['name', 'message', 'organization']
    actions = [send_emails]

admin.site.register(Feedback, FeedbackAdmin)