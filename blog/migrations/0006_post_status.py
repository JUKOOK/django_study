# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-02-22 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn'), ('a', 'another_ex')], default='d', max_length=1),
            preserve_default=False,
        ),
    ]
