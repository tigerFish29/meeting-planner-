from django.contrib import admin

# Register your models here.

from .models import Meeting
from .models import Room

admin.site.register(Meeting)
admin.site.register(Room)
