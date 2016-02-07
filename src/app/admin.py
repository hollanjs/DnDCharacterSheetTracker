from django.contrib import admin
from .models import Character, PersonalityTrait, Ideals, Bonds, Flaws


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'player_name', 'race', 'char_class', 'background', 'gender']
    ordering = ['name']


admin.site.register(Character, CharacterAdmin)
admin.site.register(PersonalityTrait)
admin.site.register(Ideals)
admin.site.register(Bonds)
admin.site.register(Flaws)