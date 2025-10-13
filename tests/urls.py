# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.contrib import admin
from django.urls import path, include


register_admin = 'django.contrib.admin' in settings.INSTALLED_APPS and getattr(settings, 'REGISTER_ADMIN_APP', False)

admin_urlpatterns = [path('admin/', admin.site.urls)] if register_admin else []


urlpatterns = admin_urlpatterns + [
    path('', include('oauth_clients.urls', namespace='oauth_clients')),
]
