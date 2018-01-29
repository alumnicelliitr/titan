# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from core.models import *

admin.site.register(User)
admin.site.register(TempUser)
admin.site.register(CampusGroup)
admin.site.register(University)
admin.site.register(Company)
admin.site.register(Location)
admin.site.register(Alum)
admin.site.register(Student)
admin.site.register(UnivAlum)
admin.site.register(CompAlum)
