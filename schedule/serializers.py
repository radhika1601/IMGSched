from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from schedule.models import Meeting, User

class MeetingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    invitees = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), many=True, view_name='user-detail' )

    class Meta:
        model = Meeting
        fields = ('url', 'id','owner', 'time', 'purpose', 'invitees')

class UserSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    meetings = serializers.HyperlinkedRelatedField(many=True, view_name='meeting-detail', read_only=True)
    meeting_list_invited = MeetingSerializer(many=True, read_only=True)
    # isadmin = models.BooleanField(default=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ('url', 'id','email', 'meeting_list_invited','meetings')
