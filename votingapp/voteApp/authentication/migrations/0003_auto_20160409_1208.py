# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_account_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='is_safe',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='account',
            name='residence_lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='residence_long',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
