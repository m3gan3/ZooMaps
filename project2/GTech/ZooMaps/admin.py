from django.contrib import admin

# Register your models here.

from .models import User, Event, Tag, CommentEvent, MessageEvent
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Tag)
admin.site.register(CommentEvent)
admin.site.register(MessageEvent)