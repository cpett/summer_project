# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1450802316.688145
_enable_loop = True
_template_filename = '/home/cpett/summer_project/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['content', 'footer', 'header']


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
    return runtime._inherit_from(context, '/homepage/templates/base2.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n      \n\n        <!-- Modal SignUp-->\n        <div class="modal fade" id="signup_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n          <div class="modal-dialog">\n            <div class="modal-content">\n              <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n                <h4 class="modal-title" id="myModalLabel">Sign Up</h4>\n              </div>\n              <div class="modal-body">\n                ...\n              </div>\n                <!--\n                  <div class="modal-footer">\n                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                    <button type="button" class="btn btn-primary">Save changes</button>\n                  </div>\n                -->\n            </div>\n          </div>\n        </div>\n      <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/colonial.png" width="75%%" style="margin-left:-25px;">\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="footer">\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="header">\n\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "index.html", "line_map": {"68": 9, "69": 33, "70": 33, "40": 1, "76": 37, "82": 37, "45": 7, "50": 35, "55": 40, "88": 3, "100": 94, "28": 0, "61": 9, "94": 3}, "filename": "/home/cpett/summer_project/homepage/templates/index.html"}
__M_END_METADATA
"""
