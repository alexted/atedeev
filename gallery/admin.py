from django.contrib import admin
from .models import Elements
# Register your models here.
#admin.site.register(Elements)

class ElementsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_header": ("header",)}

admin.site.register(Elements, ElementsAdmin)