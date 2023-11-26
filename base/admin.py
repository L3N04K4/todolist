from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class TaskResource(resources.ModelResource):
    class Meta:
        model = Task

class TaskAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'complete', 'date', 'category', 'filter')
    list_filter = ('user', 'category', 'date')
    date_hierarchy = ('date')
    filter_horizontal = ('hashtag',)
    search_fields = ('title',)
    ordering = ('-user',)
    resource_class = TaskResource

admin.site.register(Task, TaskAdmin)
admin.site.register(Categories)
admin.site.register(Hashtag)
admin.site.register(Filter)
admin.site.register(Notice)
