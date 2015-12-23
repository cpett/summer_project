# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1450804189.7473516
_enable_loop = True
_template_filename = '/home/cpett/summer_project/homepage/templates/signup.edit.html'
_template_uri = 'signup.edit.html'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['left', 'top', 'header', 'content']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n  <div>\n\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="row top-header">\n\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="header">\n\n  </div>\n')
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
        __M_writer('\n  <div class="content row">\n    <div class="col-md-6">\n\n    <div class="container">\n      <div class="row">\n        <div class="col-md-6">\n          <img  width=100% src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/signup.jpg">\n\n        <div class="cold-md-6">\n        <label>Hey! So glad you are thinking about joinging and participating in my little project. Who really knows where this project will take me, but I plan on turning it into something cool. At the very least, I will sure learn alot!</>\n        </div>\n      </div>\n    </div>\n\n    </div>\n    </div>\n    <div class="col-md-6 right">\n      <form method="POST">\n        <table>\n          ')
        __M_writer(str( form ))
        __M_writer(' \n        </table>\n        <br>\n        <button type="submit" class="btn btn-primary">Save</button>\n        <a href="/homepage/signup.delete/')
        __M_writer(str( user.id ))
        __M_writer('" class="btn btn-danger">Delete</a>\n      </form>\n    </div>\n\n  </div\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "signup.edit.html", "line_map": {"64": 50, "100": 3, "118": 41, "70": 15, "76": 15, "106": 21, "44": 1, "49": 7, "82": 9, "115": 21, "116": 28, "117": 28, "54": 13, "119": 41, "88": 9, "120": 45, "121": 45, "59": 19, "28": 0, "94": 3, "127": 121}, "filename": "/home/cpett/summer_project/homepage/templates/signup.edit.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
