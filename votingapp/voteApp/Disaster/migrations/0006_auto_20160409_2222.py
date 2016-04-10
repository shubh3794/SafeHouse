# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import swampdragon.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Disaster', '0005_auto_20160409_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notification', models.TextField()),
                ('subscriber', models.ForeignKey(related_name='subscribed', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.AddField(
            model_name='disaster',
            name='disaster_city',
            field=models.CharField(default='Delhi', max_length=100),
            preserve_default=False,
        ),
    ]
