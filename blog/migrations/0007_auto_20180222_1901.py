# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-02-22 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn'), ('a', 'Another_ex')], max_length=1),
        ),
    ]
