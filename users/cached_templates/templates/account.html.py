# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1450738809.584694
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\users\\templates/account.html'
_template_uri = 'account.html'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['top', 'content', 'header']


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
        def top():
            return render_top(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h1>')
        __M_writer(str(user.first_name))
        __M_writer('&#8217;s Account</h1>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n        <tr>\r\n          <th>ID</th>\r\n          <th>Username</th>\r\n          <th>First Name</th>\r\n          <th>Last Name</th>\r\n          <th>Email</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n')
        __M_writer('            <tr>\r\n              <td>')
        __M_writer(str( user.id ))
        __M_writer(' </td>\r\n              <td>')
        __M_writer(str( user.username ))
        __M_writer(' </td>\r\n              <td>')
        __M_writer(str( user.first_name ))
        __M_writer(' </td>\r\n              <td>')
        __M_writer(str( user.last_name ))
        __M_writer(' </td>\r\n              <td>')
        __M_writer(str( user.email ))
        __M_writer(' </td>\r\n              <td>\r\n                <a href="/users/account.edit/')
        __M_writer(str( user.id ))
        __M_writer('/" class="btn btn-success">Edit</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('      </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="header">\r\n\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"67": 9, "73": 13, "80": 13, "81": 15, "82": 15, "83": 26, "84": 27, "85": 27, "86": 28, "87": 28, "88": 29, "89": 29, "90": 30, "91": 30, "92": 31, "93": 31, "94": 33, "95": 33, "96": 37, "114": 108, "102": 3, "40": 1, "28": 0, "108": 3, "45": 7, "50": 11, "55": 39, "61": 9}, "source_encoding": "utf-8", "uri": "account.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\users\\templates/account.html"}
__M_END_METADATA
"""
