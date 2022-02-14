from django.contrib import admin

from .models import Task, Project, Goal, Tag, Context, Contact

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'folder', 'start_time')
    list_filter = ('folder', 'goal', 'context', 'tags')
    search_fields = ('title', 'note')

admin.site.register(Task, TaskAdmin)
admin.site.register(Project)
admin.site.register(Goal)
admin.site.register(Tag)
admin.site.register(Context)
admin.site.register(Contact)