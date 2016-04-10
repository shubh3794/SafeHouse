'''views exposing API to the frontend'''
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, generics, status
from Disaster.models import Disaster, willingToHelp
from django.views import generic
from authentication.models import Account
from authentication.serializers import AccountSerializer
from authentication.permissions import IsReportedBy
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Disaster.serializers import DisasterSerializer, WillToHelp, WillingToHelpSerializer
from rest_framework import mixins, views
from rest_framework.decorators import api_view
from django.db.models.functions import Coalesce


# # Create your views here.

class DisasterView(viewsets.ModelViewSet):
	'''viewset to create update and delete
	Question. Includes choices as nested data'''
	#queryset = Disaster.objects.annotate(current_sort=Coalesce('priority', 'pub_date')).order_by("-current_sort")
	queryset = Disaster.objects.all()
	serializer_class = DisasterSerializer

	def get_permissions(self):
		'''return allowed permissions'''
		if self.request.method == 'GET':
		    return (permissions.AllowAny(), )

		if self.request.method == 'POST':
		    return (permissions.AllowAny(), )

		return (IsReportedBy(), )

	def create(self, request):
		'''creates question object and assosiates it with the user'''
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			print serializer.validated_data

			ques = Disaster(
			                **serializer.validated_data)
			if request.user.pk:
				ques.reportedby = request.user
			ques.save()
			return Response(ques.id, status=status.HTTP_201_CREATED)
		else:
			#print serializer.validated_data
			return Response({'error':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

class MultiSerializerViewSet(viewsets.ModelViewSet):
    serializers = {
        'default': None,
    }

    def get_serializer_class(self):
    	print self.action
    	return self.serializers.get(self.action,
    	                            self.serializers['default'])

class HelpViewSet(MultiSerializerViewSet):
    model = willingToHelp
    queryset = willingToHelp.objects.all()

    serializers = {
        'list':    WillingToHelpSerializer,
        'detail':  WillingToHelpSerializer,
        'retrieve': WillingToHelpSerializer,
        'create': WillToHelp,
        'update': WillToHelp,
        'default':WillToHelp
    }


class GetCurrUserList(generics.ListAPIView):
	'''viewset to retrieve curr user. I have allowed only create update
	and delete methods as for each question
	choices will be provided in the Question api'''
	serializer_class = WillingToHelpSerializer
	def get_queryset(self):
		city = self.request.GET.get('city', False)
		return willingToHelp.objects.filter(user__city=city)

class GetSafeCurrUserList(generics.ListAPIView):
	'''viewset to retrieve curr user. I have allowed only create update
	and delete methods as for each question
	choices will be provided in the Question api'''
	serializer_class = AccountSerializer
	def get_queryset(self):
		city = self.request.GET.get('city', False)
		return Account.objects.filter(city=city).filter(is_safe=False)











