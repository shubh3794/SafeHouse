# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disaster', '0008_auto_20160410_0334'),
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
    ]
