# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disaster', '0007_auto_20160410_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='willingtohelp',
            name='helperdistance',
            field=models.FloatField(default=-1.0),
        ),
    ]
