# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suggest_faq', '0005_rightpredictions_wrongpredictions'),
    ]

    operations = [
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(blank=True, default='', max_length=100)),
                ('reply', models.TextField()),
                ('table', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='suggest_faq.Tables')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
