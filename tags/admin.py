from django.contrib import admin

from .models import Tag as CurrentModel

# Register your models here.

class CurrentModelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(CurrentModel, CurrentModelAdmin)
