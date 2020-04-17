# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Profil, Strangething, Comment, Like

admin.site.register(Profil)
admin.site.register(Strangething)
admin.site.register(Comment)
admin.site.register(Like)