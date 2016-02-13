from django.contrib import admin
from .models import *


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'player_name', 'race', 'char_class', 'background', 'gender']
    ordering = ['name']


admin.site.register(Character, CharacterAdmin)
admin.site.register(PersonalityTrait)
admin.site.register(Ideal)
admin.site.register(Bond)
admin.site.register(Flaw)
admin.site.register(Language)
admin.site.register(Gender)
admin.site.register(CharClass)
admin.site.register(Background)
admin.site.register(Race)