# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


class EventImageAdmin(admin.ModelAdmin):
    pass


class EventImageInline(admin.StackedInline):
    model = EventImage
    max_num = 10
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]


admin.site.register(EventImage, EventImageAdmin)
admin.site.register(Event, EventAdmin)

# Register your models here.
admin.site.register(NewsLetter)
admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Mou)
admin.site.register(Publication)
