# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1433722522.794555
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\users\\templates/signup.edit.html'
_template_uri = 'signup.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'top', 'header', 'left']


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
        def header():
            return render_header(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="content row">\r\n    <div class="col-md-6">\r\n\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-6">\r\n          <img  width=100% src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/signup.jpg">\r\n\r\n        <div class="cold-md-6">\r\n        <label>Hey! So glad you are thinking about joinging and participating in my little project. Who really knows where this project will take me, but I plan on turning it into something cool. At the very least, I will sure learn alot!</>\r\n        </div>\r\n      </div>\r\n    </div>\r\n\r\n    </div>\r\n    </div>\r\n    <div class="col-md-6 right">\r\n      <form id="signup" method="POST">\r\n        <table>\r\n          ')
        __M_writer(str( form ))
        __M_writer(' \r\n        </table>\r\n        <br>\r\n        <button type="submit" class="btn btn-primary">Save</button>\r\n        <a href="/homepage/index" class="btn btn-success">Home</a>\r\n        <a href="/homepage/signup.delete/')
        __M_writer(str( user.id ))
        __M_writer('" class="btn btn-danger">Delete</a>\r\n      </form>\r\n    </div>\r\n\r\n  </div\r\n')
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


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div>\r\n\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"96": 9, "80": 28, "69": 21, "102": 3, "43": 1, "108": 3, "114": 15, "78": 21, "79": 28, "48": 7, "81": 41, "82": 41, "83": 46, "84": 46, "53": 13, "120": 15, "58": 19, "27": 0, "90": 9, "126": 120, "63": 51}, "uri": "signup.edit.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\users\\templates/signup.edit.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
