# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disaster', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disaster',
            name='disaster_lat',
        ),
        migrations.RemoveField(
            model_name='disaster',
            name='disaster_long',
        ),
        migrations.RemoveField(
            model_name='disaster',
            name='disaster_radius',
        ),
        migrations.RemoveField(
            model_name='disaster',
            name='priority',
        ),
    ]
