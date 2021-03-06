# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160212_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archetype', models.CharField(max_length=40)),
                ('char_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.CharClass')),
            ],
            options={
                'verbose_name': 'Archetype',
                'verbose_name_plural': 'Archetypes',
            },
        ),
        migrations.AddField(
            model_name='character',
            name='archetype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Archetype'),
        ),
    ]
