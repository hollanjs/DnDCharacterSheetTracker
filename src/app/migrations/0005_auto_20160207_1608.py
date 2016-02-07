# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160207_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalityTrait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trait', models.CharField(max_length=120)),
                ('character', models.ManyToManyField(to='app.Character')),
            ],
            options={
                'verbose_name': 'PersonalityTrait',
                'verbose_name_plural': 'PersonalityTraits',
            },
        ),
        migrations.RemoveField(
            model_name='personalitytraits',
            name='character',
        ),
        migrations.RemoveField(
            model_name='bonds',
            name='character',
        ),
        migrations.AddField(
            model_name='bonds',
            name='character',
            field=models.ManyToManyField(to='app.Character'),
        ),
        migrations.RemoveField(
            model_name='flaws',
            name='character',
        ),
        migrations.AddField(
            model_name='flaws',
            name='character',
            field=models.ManyToManyField(to='app.Character'),
        ),
        migrations.RemoveField(
            model_name='ideals',
            name='character',
        ),
        migrations.AddField(
            model_name='ideals',
            name='character',
            field=models.ManyToManyField(to='app.Character'),
        ),
        migrations.DeleteModel(
            name='PersonalityTraits',
        ),
    ]