from django.contrib import admin
from .models import *

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'user', 'is_complete', )
    list_display = ('title', 'description', 'user', 'time_created', 'is_complete', )


admin.site.register(Task, TaskAdmin)
