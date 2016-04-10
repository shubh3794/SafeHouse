# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disaster', '0011_auto_20160410_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disaster',
            name='pub_date',
        ),
    ]
