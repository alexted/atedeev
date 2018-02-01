from django.contrib import admin

from .models import Feedback
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'datetime', 'email')
    list_filter = ['datetime']
    search_fields = ['name', 'message', 'organization']

admin.site.register(Feedback, FeedbackAdmin)