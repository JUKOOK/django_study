# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-03-04 09:51
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20, verbose_name='작성자')),
                ('title', models.CharField(help_text='포스팅 제목을 최대 50자 이내로 입력해주세요.', max_length=50, verbose_name='제목')),
                ('slug', models.SlugField(blank=True, help_text='포스트 제목의 별칭입니다. 한 단어만!', unique=True, verbose_name='Slug')),
                ('content', models.TextField(help_text='포스트 내용', verbose_name='내용')),
                ('description', models.CharField(blank=True, help_text='포스트 내용 한 줄 설명', max_length=100, verbose_name='한 줄 요약')),
                ('tags', models.CharField(blank=True, max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='Modify Date')),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn'), ('a', 'Another_ex')], max_length=1, verbose_name='상태')),
                ('lnglat', models.CharField(blank=True, help_text='경도, 위도 포맷으로 입력 바람', max_length=40, validators=[blog.models.lnglat_validator])),
            ],
            options={
                'verbose_name_plural': 'posts',
                'verbose_name': 'post',
                'ordering': ('-modify_date',),
                'db_table': 'my_post',
            },
        ),
    ]
