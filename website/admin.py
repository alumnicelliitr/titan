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
admin.site.register(Initiative)
admin.site.register(VideoRepository)
admin.site.register(Video)
admin.site.register(Course)
admin.site.register(Headline)
admin.site.register(Node)
admin.site.register(AlumniCard)
admin.site.register(CurrentBatchAlumniCard)
admin.site.register(ShareYourStory)
# admin.site.register()
admin.site.register(KnowYourAlumni)
admin.site.register(Award)
admin.site.register(DonationScheme)
admin.site.register(News)