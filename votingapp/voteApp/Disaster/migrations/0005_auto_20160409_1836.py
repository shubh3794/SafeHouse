# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disaster', '0004_auto_20160409_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disaster',
            name='disaster_radius',
        ),
        migrations.RemoveField(
            model_name='willingtohelp',
            name='user_loc_lat',
        ),
        migrations.RemoveField(
            model_name='willingtohelp',
            name='user_loc_long',
        ),
        migrations.AddField(
            model_name='willingtohelp',
            name='helperdistance',
            field=models.FloatField(default=9223372036854775807),
        ),
    ]
