from django.db import models
from django.contrib.auth.models import User


class Character(models.Model):
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
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('A', 'Asexual'),
        ('N', 'Not Defined'),
    )
    name            = models.CharField(max_length=40)
    player_name     = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    level           = models.IntegerField(default=1)
    xp              = models.IntegerField(default=0)
    xp_next_level   = models.IntegerField(default=0)
    race            = models.CharField(max_length=15, choices=RACES, default='Human')
    char_class      = models.CharField(max_length=10, choices=CLASSES, default='Fighter')
    background      = models.CharField(max_length=15, choices=BACKGROUNDS, default='None')
    gender          = models.CharField(max_length=1, choices=GENDERS, default='N')
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
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'

    def __str__(self):
        return '%s' % self.name


class PersonalityTrait(models.Model):
    character = models.ForeignKey(Character, null=True, blank=False)
    trait = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'PersonalityTrait'
        verbose_name_plural = 'PersonalityTraits'

    def __str__(self):
        return '%s' % self.trait


class Ideal(models.Model):
    character = models.ForeignKey(Character, null=True, blank=False)
    ideal = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Ideal'
        verbose_name_plural = 'Ideals'

    def __str__(self):
        return '%s' % self.ideal


class Bond(models.Model):
    character = models.ForeignKey(Character, null=True, blank=False)
    bond = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Bond'
        verbose_name_plural = 'Bonds'

    def __str__(self):
        return '%s' % self.bond


class Flaw(models.Model):
    character = models.ForeignKey(Character, null=True, blank=False)
    flaw = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Flaw'
        verbose_name_plural = 'Flaws'

    def __str__(self):
        return '%s' % self.flaw

class Language(models.Model):
    lang = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"

    def __str__(self):
        return '%s' % self.lang

