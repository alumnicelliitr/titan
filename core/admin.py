# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.html import format_html
from core.models import *

admin.site.register(Skill)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Organisation)
admin.site.register(Location)
admin.site.register(Alumni)
admin.site.register(Social)
admin.site.register(UserLocation)
admin.site.register(Experience)



def admin_change_url(obj):
    app_label = obj._meta.app_label
    model_name = obj._meta.model.__name__.lower()
    return reverse('admin:{}_{}_change'.format(
        app_label, model_name
    ), args=(obj.pk,))

def admin_link(attr, short_description, empty_description="-"):
    """Decorator used for rendering a link to a related model in
    the admin detail page.

    attr (str):
        Name of the related field.
    short_description (str):
        Name if the field.
    empty_description (str):
        Value to display if the related field is None.

    The wrapped method receives the related object and should 
    return the link text.

    Usage:
        @admin_link('credit_card', _('Credit Card'))
        def credit_card_link(self, credit_card):
            return credit_card.name
    """
    def wrap(func):
        def field_func(self, obj):
            related_obj = getattr(obj, attr)
            if related_obj is None:
                return empty_description
            url = admin_change_url(related_obj)
            return format_html(
                '<a href="{}">{}</a>',
                url,
                func(self, related_obj)
            )
        field_func.short_description = short_description
        field_func.allow_tags = True
        return field_func
    return wrap

from django.contrib.auth.admin import UserAdmin

class AlumniInline(admin.StackedInline):
    model = Alumni
    can_delete = False
    show_change_link = True
    verbose_name_plural = 'Alumni'
    fk_name = 'user'

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('enr_no','name', 'branch', 'course', 'alum_link',)
    list_select_related = (
        'alum',
    )
    inlines = [AlumniInline]
    model = User
    @admin_link('alum',('Alumni'))
    def alum_link(self, alum):
        return alum

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user','is_subscribed')
    list_filter = ('is_subscribed',)

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('email','is_subscribed')
    list_filter = ('is_subscribed',)


class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('subject','created_on','send_url_field' )
    def send_url_field(self, obj):
        return '<a href="%s">%s</a>' % (reverse('Core:sendmsg', kwargs={'id':obj.id,}),'Send All',)
    send_url_field.allow_tags = True
    send_url_field.short_description = 'Send all'

admin.site.register(User, CustomUserAdmin)
admin.site.register(EmailMessage, EmailMessageAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Visitor, VisitorAdmin)


