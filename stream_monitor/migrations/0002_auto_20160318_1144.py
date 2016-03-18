# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream_monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('start', models.DateTimeField()),
                ('stop', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stream_monitor.Project')),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stream_monitor.Target'),
        ),
        migrations.AddField(
            model_name='hit',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stream_monitor.Session'),
        ),
        migrations.AddField(
            model_name='hit',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stream_monitor.Track'),
        ),
    ]
