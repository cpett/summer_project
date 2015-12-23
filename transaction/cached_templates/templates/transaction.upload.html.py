# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1450886027.84785
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\transaction\\templates/transaction.upload.html'
_template_uri = 'transaction.upload.html'
_source_encoding = 'utf-8'
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
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <div class="col-sm-6 col-md-6 col-lg-6">\r\n        <h2 class="manage">Transaction Sheet</h2>\r\n      </div>\r\n      <div class="clearfix"></div>\r\n      <br/>\r\n      <div class="col-sm-6 col-md-6 col-lg-6">\r\n        This site accepts the CSV output from <a href="http://mint.com">Mint.com</a>. Once logged in to Mint, go to the\r\n        "Transactions" tab. At the bottom of the list of transactions, there will be a link that says, "Export all <i>n</i> transactions".\r\n        Click there to download a CSV that you can upload here.\r\n        <br/>\r\n        <br/>\r\n        <form method="POST" enctype="multipart/form-data">\r\n          <table>\r\n            ')
        __M_writer(str( form ))
        __M_writer('\r\n          </table>\r\n          <br>\r\n          <button type="submit" class="btn btn-success">Submit</button>\r\n          <a href="/transaction/transaction/" class="btn btn-primary">Back</a>\r\n        </form>\r\n      </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"36": 1, "54": 3, "55": 18, "56": 18, "41": 26, "28": 0, "62": 56, "47": 3}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\transaction\\templates/transaction.upload.html", "uri": "transaction.upload.html"}
__M_END_METADATA
"""
