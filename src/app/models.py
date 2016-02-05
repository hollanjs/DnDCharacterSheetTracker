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
	name = models.CharField(max_length = 50, null = False, blank = False)
	level = models.PositiveIntegerField(default = 1)
	char_class = models.CharField(max_length = 30, null = False, blank = False) # udpate later to choice field
	background = models.CharField(max_length = 20, null = True, blank = True) # udpate later to choice field
	player = models.CharField(max_length = 30, null = True, blank = True) # choices should be from users table
	race = models.CharField(max_length = 20, null = False, blank = False) # udpate later to choice field
	alignment = models.CharField(max_length = 30, default = 'Neutral', null = False, blank = False) # udpate later to choice field
	exp_points = models.PositiveIntegerField(default = 0)

	# ATTRIBUTES
	strength = models.PositiveIntegerField(default = 10)
	# strength_bonus = (self.strength - 10) // 2 

	dexterity = models.PositiveIntegerField(default = 10)
	# dexterity_bonus = (self.dexterity - 10) // 2 

	constitution = models.PositiveIntegerField(default = 10)
	# constitution_bonus = (self.constitution - 10) // 2 

	intelligence = models.PositiveIntegerField(default = 10)
	# intelligence_bonus = (self.intelligence - 10) // 2 

	wisdom = models.PositiveIntegerField(default = 10)
	# wisdom_bonus = (self.wisdom - 10) // 2 

	charisma = models.PositiveIntegerField(default = 10)
	# charisma_bonus = (self.charisma - 10) // 2 



	class Meta:
		verbose_name = 'Character'
		verbose_name_plural = 'Characters'

	def __str__(self):
		return '%s' % self.name

