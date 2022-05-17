from django.contrib import admin
from . import models

# Register your models here.
# Register your models here.
class SpacySujet(admin.ModelAdmin):
  list = ('spacy_model', 'sujet_name')

admin.site.register(models.SpacySujet, SpacySujet)