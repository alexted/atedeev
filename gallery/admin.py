from django.contrib import admin
from .models import Elements, Images
# Register your models here.
#admin.site.register(Elements)

class PostPictureInline(admin.TabularInline):
    model = Images
    fields = ['image',]

class ElementsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_header": ("header",)}
    inlines = [PostPictureInline, ]
    list_display = ('header', 'date_time', 'category')
    list_filter = ['date_time']
    search_fields = ['']

admin.site.register(Elements, ElementsAdmin)

