# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(blank=True, default='', max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('table_name', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.CharField(blank=True, default='', max_length=100)),
                ('password', models.CharField(blank=True, default='', max_length=100)),
                ('api_key', models.CharField(blank=True, default='', max_length=20)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='tables',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suggest_faq.Users'),
        ),
    ]
