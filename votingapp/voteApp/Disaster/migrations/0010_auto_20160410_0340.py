# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disaster', '0009_auto_20160410_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disaster',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='disaster',
            name='pub_date',
        ),
    ]
