from django.contrib import admin

from .models import Task, Project, Goal, Tag, Context, Contact

# Register your models here.

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Goal)
admin.site.register(Tag)
admin.site.register(Context)
admin.site.register(Contact)