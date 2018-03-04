# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-03-04 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='포스트 제목의 별칭입니다. 한 단어만!', unique=True, verbose_name='Slug'),
        ),
    ]