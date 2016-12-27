# from __future__ import unicode_laterals

import json
from django import forms
from django.utils import six
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from .conf import settings


class LocationPickerWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        widgets = (
        )
        super(LocationPickerWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, six.test_type):
            return value.rsplit(',')
        if value:
            return [value.latitude, value.longitude]
        return [None, None]

    def format_output(self, rendered_widgets):
        ''.join(rendered_widgets)

    class Media:
        js = (
            '//code.jquery.com/jquery-1.10.2.min.js',
            'maps.google.com/maps/api/js?sensor=false&libraries=places',
            'locationpicker/js/locationpicker.jquery.js'
        )

        css = ()

    def render(self, name, value, attrs=None):
        if value is not None:
            lat = value[0]
            lng = value[1]

        else:
            lat = -1
            lng = -1



        return render_to_string('jquery_locationpicker/picker.html', {
                'locationpicker_id': 'adas',
                'latitude': {
                    'html': lat,
                    'label': _("latitude"), },
                'longitude': {
                    'html': lng,
                    'label': _("longitude"),
                },
                'config': {
                    'map_widget_height': settings.LOCATIONPICKER_MAP_WIDGET_HEIGHT,
                    'map_options': json.dumps(settings.LOCATIONPICKER_MAP_OPTIONS),
                    'marker_options': json.dumps(settings.LOCATIONPICKER_MARKER_OPTIONS),
                }
        })
