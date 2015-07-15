# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1434204303.446055
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\transaction\\templates/transaction.sheet.html'
_template_uri = 'transaction.sheet.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        trans = context.get('trans', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Transaction Sheet</h2>\r\n      <div class="clearfix"></div>\r\n      <div class="text-right">\r\n        <a href="/transaction/transaction.upload/" class="btn btn-primary">Upload</a>\r\n      </div>\r\n      <br>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n        <tr>\r\n            <th>Date</th>\r\n            <th>Description</th>\r\n            <th>Amount</th>\r\n            <th>Category</th>\r\n            <th>Account Name</th>\r\n        </tr>\r\n')
        for tran in trans:
            __M_writer('        <tr>\r\n          <td>')
            __M_writer(str( tran.date ))
            __M_writer(' </td>\r\n          <td>')
            __M_writer(str( tran.description ))
            __M_writer(' </td>\r\n          <td>')
            __M_writer(str( tran.amount ))
            __M_writer(' </td>\r\n          <td>')
            __M_writer(str( tran.category ))
            __M_writer(' </td>\r\n          <td>')
            __M_writer(str( tran.Account ))
            __M_writer(' </td>\r\n        </tr>\r\n')
        __M_writer('\r\n      </table>\r\n\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\transaction\\templates/transaction.sheet.html", "line_map": {"64": 25, "65": 28, "35": 1, "71": 65, "45": 3, "27": 0, "52": 3, "53": 19, "54": 20, "55": 21, "56": 21, "57": 22, "58": 22, "59": 23, "60": 23, "61": 24, "62": 24, "63": 25}, "source_encoding": "ascii", "uri": "transaction.sheet.html"}
__M_END_METADATA
"""
