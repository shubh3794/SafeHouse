'''serializes db queries into python objs for easy json conversions'''
from rest_framework import serializers
from authentication.models import Account
from swampdragon.serializers.model_serializer import ModelSerializer


class AccountSerializer(serializers.ModelSerializer):
    '''serializer for auth users'''
    
    permission_classes = ('IsAuthenticated', 'IsAccountOwner')
    class Meta:
        '''Meta Data'''
        model = Account
        read_only_fields = ('id', 'date_joined', 'updated_at',
                            'reported')
