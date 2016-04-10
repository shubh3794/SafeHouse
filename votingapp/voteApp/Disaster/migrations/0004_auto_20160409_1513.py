# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Disaster', '0003_auto_20160409_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disaster',
            name='reportedby',
            field=models.ForeignKey(related_name='reported', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
