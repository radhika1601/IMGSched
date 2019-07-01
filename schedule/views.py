from django.shortcuts import render
from rest_framework import mixins, generics, renderers, viewsets, permissions
from schedule.models import Meeting, User
from schedule.serializers import MeetingSerializer, UserSerializer
from schedule.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from social_django.utils import psa


def index(request):
    return render(request, 'index.html')

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This viewset automatically provides 'list' and 'detail' actions.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly,]

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
    permission_class = [IsOwnerOrReadOnly, permissions.IsAuthenticated, ]

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


