from django.contrib import admin

from .models import Task, Contact

# Register your models here.

class CurrentModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'folder', 'start_time')
    list_filter = ('folder', 'goal', 'context', 'tags')
    search_fields = ('title', 'note')

admin.site.register(Task, CurrentModelAdmin)
admin.site.register(Contact)