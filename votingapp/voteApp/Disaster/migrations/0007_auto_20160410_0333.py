# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disaster', '0006_auto_20160409_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disaster',
            name='priority',
            field=models.IntegerField(default=1000),
        ),
    ]
