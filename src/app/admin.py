from django.contrib import admin
from .models import Character

class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']
    ordering = ['name']

admin.site.register(Character, CharacterAdmin)