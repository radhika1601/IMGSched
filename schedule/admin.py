from django.contrib import admin

# Register your models here.
from .models import Meeting, User

admin.site.register(Meeting)
admin.site.register(User)