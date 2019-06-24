from django.shortcuts import render
from rest_framework import mixins, generics, renderers, viewsets, permissions
from schedule.models import Meeting, User
from schedule.serializers import MeetingSerializer, UserSerializer
from schedule.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required  
from django.conf import settings
from django.contrib.auth import login, REDIRECT_FIELD_NAME
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from social_core.utils import setting_name
from social_django.utils import psa
from social_core.actions import do_auth, do_complete, do_disconnect

def index(request):
    return render(request, 'index.html')

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This viewset automatically provides 'list' and 'detail' actions.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perfom_create(self, serializer, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

class MeetingViewSet(viewsets.ModelViewSet):
	'''
	    This viewset automatically provides 'list', 'create', 'retrieve',
	    'update' and 'destroy' actions.
	'''
	queryset = Meeting.objects.all()
	serializer_class = MeetingSerializer
	permission_class = (permissions.IsAuthenticatedOrReadOnly,
		IsOwnerOrReadOnly,)

    # @login_required
    # @psa()
    # @csrf_protect
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format = format),
		'meetings': reverse('meeting-list', request=request, format=format)
		})


