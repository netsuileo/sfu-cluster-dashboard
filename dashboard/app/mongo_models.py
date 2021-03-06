# -*- coding: utf-8 -*-
from time import time
from mongoengine import *

lengths = {
    'group_name': 30,
    'plugin': 30,
    'param': 30,
    'os': 30,
    'node_type': 20,
    'node_name': 50,
    'ip': 15,
    'description': 300
}


class MonitoringInfo(Document):
    node = StringField(max_length=lengths['node_name'])
    ip = StringField(max_length=lengths['ip'])
    plugin = StringField(max_length=lengths['plugin'])
    param = StringField(max_length=lengths['param'])
    timeout = IntField(min_value=0, default=0)


class NodeGroups(Document):
    name = StringField(max_length=lengths['group_name'])
    enabled_nodes = ListField(StringField(max_length=lengths['node_name']))


class ServerGeneralInfo(Document):
    name = StringField()
    value = StringField()
    fa_icon = StringField()
    label = StringField()


class NodeInfo(Document):
    node_ip = StringField(max_length=lengths['ip'])
    node_name = StringField(max_length=lengths['node_name'])
    node_os = StringField(max_length=lengths['os'])
    enabled_plugins = ListField(StringField(max_length=lengths['plugin']))


class ParamInfo(Document):
    plugin_name = StringField(max_length=lengths['plugin'])
    param_name = StringField(max_length=lengths['param'])
    description = StringField(max_length=lengths['description'])
    axis_y_title = StringField(max_length=20, default=param_name)
    axis_x_title = StringField(max_length=20, default="Time line")
    graph_types = ListField(StringField(max_length=30))
    default_timeout = IntField(default=10)


class PluginInfo(Document):
    plugin_name = StringField(max_length=lengths['plugin'])
    description = StringField(max_length=lengths['description'])


class LineChartMetric(DynamicEmbeddedDocument):
    timestamp = IntField(default=int(time()))
    value = FloatField(default=0.0)


class PieChartMetric(DynamicEmbeddedDocument):
    class SectorData(EmbeddedDocument):
        sector_name = StringField(max_length=30)
        value = FloatField()

    timestamp = IntField(default=int(time()))
    data = EmbeddedDocumentListField(SectorData)


class NodeData(Document):
    node_name = StringField(max_length=lengths['node_name'])
    node_ip = StringField(max_length=lengths['ip'])
    plugin_name = StringField(max_length=lengths['plugin'])
    param_name = StringField(max_length=lengths['param'])
    data = DynamicField(default=LineChartMetric)


class PreviewCostructor(Document):
    username = StringField(max_length=255)
    node_name = StringField(max_length=lengths['node_name'])
    node_ip = StringField(max_length=lengths['ip'])
    plugin_name = StringField(max_length=lengths['plugin'])
    param_name = StringField(max_length=lengths['param'])


class MonitoringNodesData(Document):
    node = StringField(max_length=lengths['node_name'])
    plugin = StringField(max_length=lengths['plugin'])
    param = StringField(max_length=lengths['param'])
    data = DynamicField()
    stamp = FloatField()


from mongoengine import connect
from datetime import datetime

connect("test_monitoring")
from app.mongo_models import MonitoringNodesData
# node = 'node1'
# plugin = 'plugin1'
# param = 'param1'
# data = [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}]
# timestamp = datetime.now()
# a = MonitoringNodesData(node=node, plugin=plugin, param=param, data=data, timestamp=timestamp)

# [{'name': 'IP', 'value': '172.20.30.11', 'fa_icon': 'fa-globe', 'label': 'IP'},
# {'name': 'CPU', 'value': 'Intel(R) Xeon(R) CPU', 'fa_icon': 'fa-cubes', 'label': 'CPU'},
# {'name': 'Cores', 'value': '8', 'fa_icon': 'fa-info', 'label': 'Cores'},
# {'name': 'OS', 'value': 'CentOS', 'fa_icon': 'fa-laptop', 'label': 'OS'},
# {'name': 'HDD', 'value': '68.4 Gb', 'fa_icon': 'fa-hdd-o', 'label': 'HDD'},
# {'name': 'RAM', 'value': '3791 Mb', 'fa_icon': 'fa-bars', 'label': 'RAM'}]
