from django.db import models
from django.contrib.auth.models import User

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
	player_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
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

	strength = models.IntegerField(default=10)
	dexterity = models.IntegerField(default=10)
	constitution = models.IntegerField(default=10)
	intelligence = models.IntegerField(default=10)
	wisdom = models.IntegerField(default=10)
	charisma = models.IntegerField(default=10)

	speed = models.IntegerField(default=30)

	hp_max = models.IntegerField(default=20)
	hp = models.IntegerField(default=20)
	temp_hp = models.IntegerField(default=0)


	class Meta:
		verbose_name = 'Character'
		verbose_name_plural = 'Characters'

	def __str__(self):
		return '%s' % self.name


class PersonalityTraits(models.Model):
	trait = models.CharField(max_length=120)
	character = models.ForeignKey(Character, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'PersonalityTrait'
		verbose_name_plural = 'PersonalityTraits'

	def __str__(self):
		return '%s' % self.trait


class Ideals(models.Model):
	ideal = models.CharField(max_length=150)
	character = models.ForeignKey(Character, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Ideal'
		verbose_name_plural = 'Ideals'

	def __str__(self):
		return '%s' % self.ideal


class Bonds(models.Model):
	bond = models.CharField(max_length=150)
	character = models.ForeignKey(Character, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Bond'
		verbose_name_plural = 'Bonds'

	def __str__(self):
		return '%s' % self.bond


class Flaws(models.Model):
	flaw = models.CharField(max_length=150)
	character = models.ForeignKey(Character, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Flaw'
		verbose_name_plural = 'Flaws'

	def __str__(self):
		return '%s' % self.flaw

