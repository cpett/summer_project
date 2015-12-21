# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1450738813.008823
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\users\\templates/account.edit.html'
_template_uri = 'account.edit.html'
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
        user = context.get('user', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
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
        __M_writer('\r\n  <div class="row top-header">\r\n\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <div class="row">\r\n        <div class="col-md-6">\r\n          <img  width=100% src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/signup.jpg">\r\n\r\n        <div class="cold-md-6">\r\n        <label>This is all your account information as we have it. Feel free to make any changes or updates. You&#8217;ll notice that there isn&#8217;t a place to change your password. That&#8217;s because I don&#8217;t store your password in plain text. You&#8217;ll have to click &#8217;Change Password&#8217; to update your password.</>\r\n        </div>\r\n      </div>\r\n      <div class="col-md-6">\r\n        <form method="POST">\r\n          <table>\r\n            ')
        __M_writer(str( form ))
        __M_writer('\r\n          </table>\r\n          <br>\r\n          <button type="submit" class="btn btn-primary">Submit</button>\r\n          <a href="/users/account.password/')
        __M_writer(str( user.id ))
        __M_writer('" class="btn btn-success">Change Password</a>          \r\n          <a href="/users/account.delete/')
        __M_writer(str( user.id ))
        __M_writer('" class="btn btn-danger">Delete Account</a>\r\n      </div>\r\n      </form>\r\n    </div>\r\n')
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
{"line_map": {"98": 3, "69": 9, "104": 3, "92": 35, "42": 1, "75": 17, "89": 34, "110": 104, "47": 7, "84": 17, "85": 21, "86": 21, "57": 39, "88": 30, "52": 13, "87": 30, "91": 35, "28": 0, "90": 34, "63": 9}, "source_encoding": "utf-8", "uri": "account.edit.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\users\\templates/account.edit.html"}
__M_END_METADATA
"""
