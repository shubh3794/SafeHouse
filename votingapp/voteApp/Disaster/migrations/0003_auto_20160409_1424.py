# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disaster', '0002_auto_20160409_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='disaster',
            name='disaster_lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disaster',
            name='disaster_long',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disaster',
            name='disaster_radius',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='disaster',
            name='priority',
            field=models.IntegerField(default=10000000),
        ),
    ]
