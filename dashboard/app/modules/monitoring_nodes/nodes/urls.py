# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url, include
from .views import NodesView

urlpatterns = [
    url(r'^$', NodesView.as_view(), name='index'),
#    url(r'^(?P<node_name>.*)/graphs/', include('app.nodes.graphs.urls')),
]
