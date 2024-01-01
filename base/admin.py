from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class TaskResource(resources.ModelResource):

    class Meta:
        model = Task

    def get_user(self, task):
        user = task.user  # Получаем объект пользователя, связанного с задачей
        return user.username if user else ''  # Возвращаем имя пользователя или пустую строку, если пользователь не найден

    def dehydrate_user(self, task):
        return self.get_user(task)  # Используем кастомизированный метод для получения имени пользователя

    

class TaskAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'complete', 'date', 'category', 'filter')
    list_filter = ('user', 'category', 'date')
    date_hierarchy = ('date')
    filter_horizontal = ('hashtag',)
    search_fields = ('title',)
    ordering = ('-user',)
    resource_class = TaskResource

    def get_export_queryset(self, request):
        return Task.objects.filter(complete=True)
    
    

admin.site.register(Task, TaskAdmin)
admin.site.register(Categories)
admin.site.register(Hashtag)
admin.site.register(Filter)
admin.site.register(Notice)
