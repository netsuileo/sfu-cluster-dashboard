__author__ = 'mist'
from django.shortcuts import render
from django.views.generic import View
from dashboard.app.models import NodeInfo
from mongoengine import connect

connect("test")


class GraphsView(View):
    template_name = 'nodes/nodes.html'
    """template_name = 'nodes/nodes.html'

    def get(self, request, *args, **kwargs):
        nodes_render = []
        nodes = NodeInfo.objects()
        for node in nodes:
            new_params = []
            params = plugin.params_info
            for param in params:
                new_params.append({
                    'name': param.param_name,
                    'description': param.description,
                    'timeout': param.timeout
                })
            plugins_render.append({
                'name': plugin.plugin_name,
                'description': plugin.description,
                'params_info': new_params
            })
        print plugins_render
        return render(request, self.template_name, {'nodes': nodes_render})
"""