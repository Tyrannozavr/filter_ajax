from django.contrib import admin
from .models import Table, Genre


@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    fields = ['title']


@admin.register(Table)
class AdminTable(admin.ModelAdmin):
    fields = ['title']
