# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disaster_name', models.CharField(max_length=2000)),
                ('disaster_description', models.TextField()),
                ('disaster_type', models.CharField(max_length=10)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('disaster_lat', models.FloatField()),
                ('disaster_long', models.FloatField()),
                ('disaster_radius', models.IntegerField(default=1000)),
                ('priority', models.IntegerField(default=10000000)),
                ('reportedby', models.ForeignKey(related_name='reported', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='willingToHelp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_loc_lat', models.FloatField()),
                ('user_loc_long', models.FloatField()),
                ('disaster', models.ForeignKey(related_name='helpedby', to='Disaster.Disaster')),
                ('user', models.ForeignKey(related_name='readytohelp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
