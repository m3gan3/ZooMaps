from django.contrib import admin

# Register your models here.

from .models import User, Place, Event
admin.site.register(User)
admin.site.register(Place)
admin.site.register(Event)