'''Serializers convert the db queries into python
data structures(dictionaries) for easy json rendering'''
from rest_framework import serializers
from Disaster.models import Disaster, willingToHelp
from authentication.serializers import AccountSerializer


class DisasterSerializer(serializers.ModelSerializer):
	'''serializes choice object'''
	class Meta:
		'''defines the model to be serialized'''
		model = Disaster
		read_only = ('reportedby', 'pub_date', 'priority', )


class WillingToHelpSerializer(serializers.ModelSerializer):
	'''serializes choice object'''
	user = AccountSerializer(many=False, read_only=True)
	disaster = DisasterSerializer(many=False, read_only=True)
	class Meta:
		'''defines the model to be serialized'''
		model = willingToHelp
		read_only = ('helperdistance', )


class WillToHelp(serializers.ModelSerializer):
	'''serializes choice object'''
	class Meta:
		'''defines the model to be serialized'''
		model = willingToHelp
		read_only = ('helperdistance', )


from swampdragon.serializers.model_serializer import ModelSerializer


class TodoListSerializer(ModelSerializer):
    class Meta:
        model = 'Disaster.TodoList'
        publish_fields = ('notification', 'user')



