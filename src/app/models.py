from django.db import models


# class ClassName(models.Model):
# 	attr = models.FieldName(property)

# 	def __str__(self):
# 		return '%s' % self.something


'''
EXAMPLE OF CHOICES

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
'''


class Character(models.Model):
	name = models.CharField(max_length=40)
	player_name = models.CharField(max_length=30)
	level = models.IntegerField(default=1)
	xp = models.IntegerField(default=0)
	RACES = (
		('Dragonborn', 'Dragonborn'),
		('Drow', 'Drow'),
		('Dwarf', 'Dwarf'),
		('Elf', 'Elf'),
		('Gnome', 'Gnome'),
		('Half-elf', 'Half-elf'),
		('Half-orc', 'Half-orc'),
		('Halfling-Hobbit', 'Halfling-Hobbit'),
		('Human', 'Human'),
		('Tiefling', 'Tiefling'),
	)
	race = models.CharField(max_length=15, choices=RACES, default='Human')
	CLASSES = (
		('Cleric', 'Cleric'),
		('Fighter', 'Fighter'),
		('Rogue', 'Rogue'),
		('Wizard', 'Wizard'),
		('Barbarian', 'Barbarian'),
		('Bard', 'Bard'),
		('Druid', 'Druid'),
		('Monk', 'Monk'),
		('Paladin', 'Paladin'),
		('Ranger', 'Ranger'),
		('Sorcerer', 'Sorcerer'),
		('Warlock', 'Warlock'),
	)
	char_class = models.CharField(max_length=10, choices=CLASSES, default='Fighter')
	BACKGROUNDS = (
		('Acolyte', 'Acolyte'),
		('Criminal', 'Criminal'),
		('Charlatan', 'Charlatan'),
		('Entertainer', 'Entertainer'),
		('Folk Hero', 'Folk Hero'),
		('Guild Artisan', 'Guild Artisan'),
		('Hermit', 'Hermit'),
		('Noble', 'Noble'),
		('None', 'None'),
		('Other', 'Other'),
		('Outlander', 'Outlander'),
		('Sage', 'Sage'),
		('Sailor', 'Sailor'),
		('Soldier', 'Soldier'),
		('Urchin', 'Urchin'),
	)
	background = models.CharField(max_length=15, choices=BACKGROUNDS, default='None')
	GENDERS = (
		('M', 'Male'),
		('F', 'Female'),
		('A', 'Asexual'),
		('N', 'Not Defined'),
	)
	gender = models.CharField(max_length=1, choices=GENDERS, default='N')


	





	class Meta:
		verbose_name = 'Character'
		verbose_name_plural = 'Characters'

	def __str__(self):
		return '%s' % self.name

