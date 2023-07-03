from django.contrib import admin
from .models import Task
from .models import Categories
from .models import Hashtag
from .models import Filter
from .models import Notice

class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'complete', 'date', 'category', 'filter')
    list_filter = ('user', 'category', 'date')
    date_hierarchy = ('date')
    filter_horizontal = ('hashtag',)
    search_fields = ('title',)
    ordering = ('-user',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Categories)
admin.site.register(Hashtag)
admin.site.register(Filter)
admin.site.register(Notice)
