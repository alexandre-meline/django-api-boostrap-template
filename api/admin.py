from django.contrib import admin
from . import models

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
  list = ('title', 'description', 'completed')

admin.site.register(models.Todo, TodoAdmin)