from django.contrib import admin
from .models import Character, PersonalityTraits, Ideals, Bonds, Flaws


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'player_name', 'race', 'char_class', 'background', 'gender']
    ordering = ['name']


class PersonalityTraitsAdmin(admin.ModelAdmin):
	list_display = ['character', 'trait']
	ordering = ['character']


class IdealsAdmin(admin.ModelAdmin):
	list_display = ['character', 'ideal']
	ordering = ['character']


class BondsAdmin(admin.ModelAdmin):
	list_display = ['character', 'bond']
	ordering = ['character']


class FlawsAdmin(admin.ModelAdmin):
	list_display = ['character', 'flaw']
	ordering = ['character']


admin.site.register(Character, CharacterAdmin)
admin.site.register(PersonalityTraits, PersonalityTraitsAdmin)
admin.site.register(Ideals, IdealsAdmin)
admin.site.register(Bonds, BondsAdmin)
admin.site.register(Flaws, FlawsAdmin)