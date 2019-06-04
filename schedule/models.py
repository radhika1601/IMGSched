from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    time = models.DateTimeField()
    purpose = models.CharField(max_length=1000, blank=True, default='')
    invitees = models.ManyToManyField(User, related_name='meeting_list_invited')
    owner = models.ForeignKey('auth.User', related_name='meetings', on_delete=models.CASCADE, default=None)
    class Meta:
    	ordering = ('time', )