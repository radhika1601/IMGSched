from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
# Create your models here.

class User(AbstractUser):
	email = models.EmailField( _('email address'), unique=True)
	admin = models.BooleanField(default=False)
	USERNAME_FIELDS = 'email'
	REQUIRED_FIELDS = []
	objects = CustomUserManager()

	def __str__(self):
		return self.email

class Meeting(models.Model):
    time = models.DateTimeField()
    purpose = models.CharField(max_length=1000, blank=True, default='')
    invitees = models.ManyToManyField(User, related_name='meeting_list_invited')
    owner = models.ForeignKey(User, related_name='meetings', on_delete=models.CASCADE, default=None)
    class Meta:
    	ordering = ('time', )

