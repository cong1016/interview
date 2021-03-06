# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-23 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientid', models.CharField(db_index=True, max_length=20, verbose_name='客户端id')),
                ('grade', models.CharField(max_length=50, verbose_name='玩家分数')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'player',
            },
        ),
    ]
