from django.contrib import admin

# Register your models here.

from .models import Event, Tag, RatingEvent, MessageEvent
admin.site.register(Event)
admin.site.register(Tag)
admin.site.register(RatingEvent)
admin.site.register(MessageEvent)