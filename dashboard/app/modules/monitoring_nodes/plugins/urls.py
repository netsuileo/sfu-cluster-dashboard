# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import PluginsView

urlpatterns = [
    url(r'^$', PluginsView.as_view(), name='index'),
]