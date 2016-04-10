# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20160409_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='residence_lat',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='residence_long',
            field=models.FloatField(blank=True),
        ),
    ]
