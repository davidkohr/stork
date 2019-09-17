# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-09-17 21:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferenceID', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('preferenceID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_preferenceID', to='storkbabyapp.preferences')),
            ],
        ),
        migrations.CreateModel(
            name='userPreferenceMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferenceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userpreferencemapping_preferenceID', to='storkbabyapp.preferences')),
            ],
        ),
        migrations.CreateModel(
            name='userRelations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField(default=0)),
                ('userType', models.IntegerField(default=0)),
                ('emailAddress', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='userrelations',
            name='relatingUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrelations_relatingUser', to='storkbabyapp.users'),
        ),
        migrations.AddField(
            model_name='userrelations',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrelations_userID', to='storkbabyapp.users'),
        ),
        migrations.AddField(
            model_name='userpreferencemapping',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userpreferencemapping_userID', to='storkbabyapp.users'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='reviewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_reviewer', to='storkbabyapp.users'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_user', to='storkbabyapp.users'),
        ),
    ]
