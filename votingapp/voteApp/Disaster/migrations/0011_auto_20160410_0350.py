# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Disaster', '0010_auto_20160410_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='disaster',
            name='disaster_lat',
            field=models.FloatField(default=22.22),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disaster',
            name='disaster_long',
            field=models.FloatField(default=27.76),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disaster',
            name='priority',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='disaster',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 10, 3, 50, 2, 229351, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
