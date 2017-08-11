# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puzzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JottoWebApp.Puzzle')),
            ],
        ),
        migrations.AddField(
            model_name='guess',
            name='new_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JottoWebApp.Session'),
        ),
    ]
