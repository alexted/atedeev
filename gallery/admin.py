from django.contrib import admin
from .models import Elements, Images
from django.utils.html import mark_safe
# Register your models here.
#admin.site.register(Elements)

class PostPictureInline(admin.TabularInline):
    model = Images
    fields = ['image','get_prev_url_300']
    readonly_fields = ['get_prev_url_300']


class ElementsAdmin(admin.ModelAdmin):
    def show_preview_img(self, obj):
        return mark_safe('<img src="%s" alt="Картинка">' % (obj.get_prev_url_200()))


    prepopulated_fields = {"slug_header": ("header",)}
    inlines = [PostPictureInline, ]
    list_display = ('header', "show_preview_img" ,'date_time', 'category')
    list_filter = ['date_time']
    search_fields = ['header' ,'description', 'url']
    show_preview_img.short_description ="Preview"



admin.site.register(Elements, ElementsAdmin)

