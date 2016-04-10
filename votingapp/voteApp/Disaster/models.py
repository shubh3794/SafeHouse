from django.db import models
from django.conf import settings
from authentication.models import Account
from django.utils import timezone
import datetime
# Create your models here.
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
import math
import sys

def distance_on_unit_sphere(lat1, long1, lat2, long2):
	degrees_to_radians = math.pi/180.0

	# phi = 90 - latitude
	phi1 = (90.0 - lat1)*degrees_to_radians
	phi2 = (90.0 - lat2)*degrees_to_radians

	# theta = longitude
	theta1 = long1*degrees_to_radians
	theta2 = long2*degrees_to_radians

	cos = (math.sin(phi1) * math.sin(phi2) * \
	       math.cos(theta1 - theta2) + math.cos(phi1)*math.cos(phi2))
	arc = math.acos(cos)

	return arc*6373

class Disaster(models.Model):
	reportedby = models.ForeignKey(Account, null=True, on_delete=models.CASCADE,
	                              related_name="reported")
	disaster_name = models.CharField(max_length=2000, null=False)
	disaster_description = models.TextField()
	disaster_type = models.CharField(max_length=10)
	disaster_lat = models.FloatField(blank=False, null=False)
	disaster_long = models.FloatField(blank=False, null=False)
	disaster_city = models.CharField(max_length=100, null=False)
	priority = models.IntegerField(default=1000)
	def __unicode__(self):
		return self.disaster_name

class willingToHelp(models.Model):
	user = models.ForeignKey(Account, on_delete=models.CASCADE,
	                         related_name="readytohelp")
	disaster = models.ForeignKey(Disaster, on_delete=models.CASCADE,
	                             related_name="helpedby")
	helperdistance = models.FloatField(null=False, default=-1.0)
	def save(self, *args, **kwargs):
		self.helperdistance = distance_on_unit_sphere(self.disaster.disaster_lat,
		                                              self.disaster.disaster_long,
		                                              self.user.residence_lat,
		                                              self.user.residence_long)
		super(willingToHelp, self).save(*args, **kwargs)


from swampdragon.models import SelfPublishModel
from Disaster.serializers import TodoListSerializer


class TodoList(SelfPublishModel, models.Model):
    serializer_class = TodoListSerializer
    notification = models.TextField()
    subscriber = models.ForeignKey(Account, on_delete=models.CASCADE,
                                   related_name="subscribed")


@receiver(post_save, sender=Disaster)
def assosiate_calendar(sender, **kwargs):
    '''assosiate one to one calender to the user instance'''
    a = Account.objects.all()
    instance = kwargs['instance']
    for i in a:
    	print i.city
    	if i.city == instance.disaster_city:
    		notification = instance.disaster_name + " reported in " + \
    		instance.disaster_city + ". Are you safe?"
    		TodoList.objects.create(notification=notification, subscriber=i)
