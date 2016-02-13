from django.db import models
from django.contrib.auth.models import User


'''
THINGS TO DO:
- add weapons class to add weapons
  -  should this be one to one or many to many?
  -  maybe it should be normal weapons as many to many
     and specialty weapons as one to one...
  -  use this site: http://5edndwiki.wikidot.com/equipment-weapons
'''



class Race(models.Model):
    race = models.CharField(max_length=20)

    class Meta:
        verbose_name        = "Race"
        verbose_name_plural = "Races"

    def __str__(self):
        return '%s' % self.race


class CharClass(models.Model):
    char_class = models.CharField(max_length=20)

    class Meta:
        verbose_name        = "Character Class"
        verbose_name_plural = "Character Classes"

    def __str__(self):
        return '%s' % self.char_class


class Background(models.Model):
    background = models.CharField(max_length=20)

    class Meta:
        verbose_name        = "Background"
        verbose_name_plural = "Backgrounds"

    def __str__(self):
        return '%s' % self.background


class Gender(models.Model):
    gender = models.CharField(max_length=12)

    class Meta:
        verbose_name        = "Gender"
        verbose_name_plural = "Genders"

    def __str__(self):
        return '%s' % self.gender


class Archetype(models.Model):
    archetype  = models.CharField(max_length=40)
    char_class = models.ForeignKey(CharClass, null=True, blank=False)

    class Meta:
        verbose_name        = "Archetype"
        verbose_name_plural = "Archetypes"

    def __str__(self):
        return '%s' % self.archetype
                                            

class Character(models.Model):
    name            = models.CharField(max_length=40)
    player_name     = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    level           = models.IntegerField(default=1)
    xp              = models.IntegerField(default=0)
    xp_next_level   = models.IntegerField(default=0)
    race            = models.ForeignKey(Race, null=True, blank=False)
    char_class      = models.ForeignKey(CharClass, null=True, blank=False)
    archetype       = models.ForeignKey(Archetype, null=True, blank=True)
    background      = models.ForeignKey(Background, null=True, blank=False)
    gender          = models.ForeignKey(Gender, null=True, blank=False)
    # traits          = models.ManyToManyField('PersonalityTrait')
    # ideals          = models.ManyToManyField('Ideals')
    # bonds           = models.ManyToManyField('Bonds')
    # flaws           = models.ManyToManyField('Flaws')
    languages       = models.ManyToManyField('language')
    hair            = models.CharField(max_length=50, null=True, blank=False)
    eyes            = models.CharField(max_length=10, null=True, blank=False)
    skin            = models.CharField(max_length=20, null=True, blank=False)
    height          = models.IntegerField(default=100)
    weight          = models.IntegerField(default=100)
    size            = models.CharField(max_length=20, default='Medium')
    distinguishing_marks = models.TextField(null=True, blank=False)
    diety           = models.CharField(max_length=50, null=True, blank=True)
    domain          = models.CharField(max_length=50, null=True, blank=True)
    organization    = models.CharField(max_length=50, null=True, blank=True)
    downtime        = models.CharField(max_length=50, null=True, blank=True)
    lifestyle       = models.CharField(max_length=50, null=True, blank=True)
    piety           = models.IntegerField(default=0)
    honor           = models.IntegerField(default=0)
    vision          = models.IntegerField(default=0)
    strength        = models.IntegerField(default=10)
    str_proficiency = models.BooleanField(default=False)
    str_advantage   = models.BooleanField(default=False)
    str_expertise   = models.BooleanField(default=False)
    dexterity       = models.IntegerField(default=10)
    dex_proficiency = models.BooleanField(default=False)
    dex_advantage   = models.BooleanField(default=False)
    dex_expertise   = models.BooleanField(default=False)
    constitution    = models.IntegerField(default=10)
    con_proficiency = models.BooleanField(default=False)
    con_advantage   = models.BooleanField(default=False)
    con_expertise   = models.BooleanField(default=False)
    intelligence    = models.IntegerField(default=10)
    int_proficiency = models.BooleanField(default=False)
    int_advantage   = models.BooleanField(default=False)
    int_expertise   = models.BooleanField(default=False)
    wisdom          = models.IntegerField(default=10)
    wis_proficiency = models.BooleanField(default=False)
    wis_advantage   = models.BooleanField(default=False)
    wis_expertise   = models.BooleanField(default=False)
    charisma        = models.IntegerField(default=10)
    cha_proficiency = models.BooleanField(default=False)
    cha_advantage   = models.BooleanField(default=False)
    cha_expertise   = models.BooleanField(default=False)
    speed           = models.IntegerField(default=30)
    armor           = models.IntegerField(default=10)
    hp_max          = models.IntegerField(default=20)
    hp              = models.IntegerField(default=20)
    temp_hp         = models.IntegerField(default=0)


    class Meta:
        verbose_name        = 'Character'
        verbose_name_plural = 'Characters'

    def __str__(self):
        return '%s' % self.name


class PersonalityTrait(models.Model):
    character = models.ForeignKey(Character, null=True, blank=False)
    trait = models.CharField(max_length=120)

    class Meta:
        verbose_name        = 'PersonalityTrait'
        verbose_name_plural = 'PersonalityTraits'

    def __str__(self):
        return '%s' % self.trait


class Ideal(models.Model):
    character = models.ForeignKey(Character, null=True, blank=False)
    ideal = models.CharField(max_length=150)

    class Meta:
        verbose_name        = 'Ideal'
        verbose_name_plural = 'Ideals'

    def __str__(self):
        return '%s' % self.ideal


class Bond(models.Model):
    character = models.ForeignKey(Character, null=True, blank=False)
    bond = models.CharField(max_length=150)

    class Meta:
        verbose_name        = 'Bond'
        verbose_name_plural = 'Bonds'

    def __str__(self):
        return '%s' % self.bond


class Flaw(models.Model):
    character = models.ForeignKey(Character, null=True, blank=False)
    flaw = models.CharField(max_length=150)

    class Meta:
        verbose_name        = 'Flaw'
        verbose_name_plural = 'Flaws'

    def __str__(self):
        return '%s' % self.flaw

class Language(models.Model):
    lang = models.CharField(max_length=20)

    class Meta:
        verbose_name        = "Language"
        verbose_name_plural = "Languages"

    def __str__(self):
        return '%s' % self.lang

