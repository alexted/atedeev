from django.contrib import admin
from .models import Project, Screenshot, Video
from django.utils.html import mark_safe

# Register your models here.
class ProjectPictureInline(admin.TabularInline):
    model = Screenshot

    def get_resized_preview_image_html(self, obj):
        return mark_safe('<img src="%s" alt="Картинка">' % (obj.get_resized_screenshot_url_300()))

    get_resized_preview_image_html.short_description = 'Миниатюра'
    fields = ['image','get_resized_preview_image_html']
    readonly_fields = ['get_resized_preview_image_html']

class ProjectVideoInline(admin.TabularInline):
    model = Video

class ProjectAdmin(admin.ModelAdmin):
    def get_resized_preview_screenshot_html(self, obj):
        return mark_safe('<img src="%s" alt="Картинка">' % (obj.get_resized_screenshot_200()))

    prepopulated_fields = {"slug_header": ("header",)}
    inlines = [ProjectPictureInline, ProjectVideoInline]
    list_display = ('header',
                    "get_resized_preview_screenshot_html",
                    'creation_date_time',
                    'category')
    list_filter = ['creation_date_time']
    search_fields = ['header', 'description', 'url']
    get_resized_preview_screenshot_html.short_description ="Preview"



admin.site.register(Project, ProjectAdmin)

