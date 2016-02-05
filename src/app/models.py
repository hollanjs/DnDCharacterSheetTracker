from django.db import models


# class ClassName(models.Model):
# 	attr = models.FieldName(property)

# 	def __str__(self):
# 		return '%s' % self.something


class Character(models.Model):
	name = models.CharField(max_length = 50)
	level = models.IntegerField()
	char_class = models.CharField(max_length = 30) # udpate later to choice fields
	background = models.CharField(max_length = 20) # udpate later to choice fields
	player = models.CharField(max_length = 30) # choices should be from users table
	race = models.CharField(max_length = 20) # udpate later to choice fields
	alignment = models.CharField(max_length = 30) # udpate later to choice fields


	class Meta:
		verbose_name = 'Character'
		verbose_name_plural = 'Characters'

	def __str__(self):
		return '%s' % self.name


class ClassName(models.Model):
	attr = models.FieldName(property)

	def __str__(self):
		return '%s' % self.something