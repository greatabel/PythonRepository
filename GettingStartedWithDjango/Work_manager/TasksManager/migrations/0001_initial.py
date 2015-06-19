# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'Title')),
                ('description', models.CharField(max_length=1000, verbose_name=b'description')),
                ('client_name', models.CharField(max_length=1000, verbose_name=b'Client name')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'Title')),
                ('description', models.CharField(max_length=1000, verbose_name=b'Description')),
                ('time_elapsed', models.IntegerField(default=None, null=True, verbose_name=b'Elapsed time', blank=True)),
                ('importance', models.IntegerField(verbose_name=b'Importance')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('login', models.CharField(max_length=25, verbose_name=b'Login')),
                ('password', models.CharField(max_length=100, verbose_name=b'Password')),
                ('phone', models.CharField(default=None, max_length=20, null=True, verbose_name=b'Phone number', blank=True)),
                ('born_date', models.DateField(default=None, null=True, verbose_name=b'Born date', blank=True)),
                ('last_connection', models.DateTimeField(default=None, null=True, verbose_name=b'Date of last   connection', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('years_seniority', models.IntegerField(default=0, verbose_name=b'Seniority')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name=b'Date of Birthday')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('userprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='TasksManager.UserProfile')),
            ],
            bases=('TasksManager.userprofile',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='TasksManager.UserProfile')),
                ('specialisation', models.CharField(max_length=50, verbose_name=b'Specialisation')),
            ],
            bases=('TasksManager.userprofile',),
        ),
        migrations.AddField(
            model_name='task',
            name='app_user',
            field=models.ForeignKey(verbose_name=b'User', to='TasksManager.UserProfile'),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=None, blank=True, to='TasksManager.Project', null=True, verbose_name=b'Project'),
        ),
        migrations.AddField(
            model_name='developer',
            name='supervisor',
            field=models.ForeignKey(verbose_name=b'Supervisor', to='TasksManager.Supervisor'),
        ),
    ]
