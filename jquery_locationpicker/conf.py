# -*- coding: utf-8 -*-

from django.conf import settings

class LocationPickerConf(object):

    MAP_WIDGET_HEIGHT = 480
    MAP_OPTIONS = {}
    MARKER_OPTIONS = {}

    class Meta:
        prefix = 'locationpicker'
