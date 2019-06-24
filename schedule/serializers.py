from rest_framework import serializers
from schedule.models import Meeting
from django.contrib.auth.models import User

class MeetingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    invitees = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), many=True, view_name='user-detail')

    class Meta:
        model = Meeting
        fields = ('url', 'id','owner', 'time', 'purpose', 'invitees')

class UserSerializer(serializers.ModelSerializer):
    
    meetings = serializers.HyperlinkedRelatedField(many=True, view_name='meeting-detail', read_only=True)
    meeting_list_invited = MeetingSerializer(many=True, read_only=True)
    # isadmin = models.BooleanField(default=False)

    class Meta:
        model = User
        fields = ('url', 'username', 'id', 'meeting_list_invited','meetings')
