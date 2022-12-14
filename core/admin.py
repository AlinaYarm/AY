from django.contrib import admin
from core import models

@admin.register(models.Person)
class Person(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_field = ('name')
