# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-08 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import photo.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('description', models.CharField(blank=True, max_length=80, verbose_name='한 줄 요약')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='제목')),
                ('image', photo.fields.ThumbnailImageField(upload_to='photo/%/%m')),
                ('content', models.TextField(blank=True, verbose_name='사진 요약')),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='upload_date')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.Album')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
