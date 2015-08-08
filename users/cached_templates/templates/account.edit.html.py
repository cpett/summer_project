# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438977386.425757
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\users\\templates/account.edit.html'
_template_uri = 'account.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['top', 'header', 'content']


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
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        user = context.get('user', UNDEFINED)
        form = context.get('form', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"uri": "account.edit.html", "line_map": {"96": 21, "97": 21, "98": 30, "99": 30, "68": 9, "101": 34, "102": 35, "103": 35, "41": 1, "74": 3, "109": 103, "46": 7, "80": 3, "51": 13, "86": 17, "56": 39, "100": 34, "27": 0, "62": 9, "95": 17}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\users\\templates/account.edit.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
