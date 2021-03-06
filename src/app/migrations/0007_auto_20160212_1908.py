# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 00:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160211_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Languages',
                'verbose_name': 'Language',
            },
        ),
        migrations.RemoveField(
            model_name='character',
            name='bonds',
        ),
        migrations.RemoveField(
            model_name='character',
            name='flaws',
        ),
        migrations.RemoveField(
            model_name='character',
            name='ideals',
        ),
        migrations.RemoveField(
            model_name='character',
            name='traits',
        ),
        migrations.AddField(
            model_name='bonds',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Character'),
        ),
        migrations.AddField(
            model_name='flaws',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Character'),
        ),
        migrations.AddField(
            model_name='ideals',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Character'),
        ),
        migrations.AddField(
            model_name='personalitytrait',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Character'),
        ),
        migrations.AddField(
            model_name='character',
            name='languages',
            field=models.ManyToManyField(to='app.Language'),
        ),
    ]
