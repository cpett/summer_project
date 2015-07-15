# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1435498843.614016
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\dashboard\\templates/dashboard.data.json'
_template_uri = 'dashboard.data.json'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        acc_json = context.get('acc_json', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str(acc_json))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "28": 22, "22": 1}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\dashboard\\templates/dashboard.data.json", "uri": "dashboard.data.json", "source_encoding": "ascii"}
__M_END_METADATA
"""
