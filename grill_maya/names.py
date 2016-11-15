# -*- coding: utf-8 -*-
"""
Maya names for grill data.
"""
from grill.names import Name


class MyAttribute(Name):
    """docstring for MyAttribute"""
    def _set_separator(self):
        self._separator = ''

    def _set_values(self):
        super(MyAttribute, self)._set_values()
        self._plug = '(in|out)'
        self._attribute = '[a-zA-Z]+'
        self._axis = '[XYZ]?'
        self._index = '\d?'

    def _set_patterns(self):
        super(MyAttribute, self)._set_patterns()
        self._set_pattern('plug', 'attribute', 'axis', 'index')

    def _get_pattern_list(self):
        return ['_plug', '_attribute', '_axis', '_index']
