from django.contrib import admin

from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time',)
    list_filter = ('goal', 'context',)
    search_fields = ('title', 'note',)

admin.site.register(Project, ProjectAdmin)
