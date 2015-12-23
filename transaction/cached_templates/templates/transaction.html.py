# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1443759389.298315
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\transaction\\templates/transaction.html'
_template_uri = 'transaction.html'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['header', 'top', 'footer', 'content']


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
        def header():
            return render_header(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        transaction = context.get('transaction', UNDEFINED)
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
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="header">\r\n\r\n    </div>\r\n')
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


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="footer">\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        transaction = context.get('transaction', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Transaction Index</h2>\r\n      <div class="clearfix"></div>\r\n      <br/>\r\n      <div class="row form-inline">\r\n        <div class="col-md-3">\r\n          <input type="search" class="light-table-filter form-control" data-table="order-table" placeholder="Filter">\r\n        </div>\r\n        <div class="col-md-3">\r\n        </div>\r\n        <div class="col-md-6">\r\n          <div class="text-right">\r\n            <button  id="show_instructions_dialog" class="btn btn-primary">Upload Instructions</button>\r\n            <a href="/transaction/transaction.upload/" class="btn btn-success">Upload CSV</a>\r\n            <a href="/transaction/transaction.create/" class="btn btn-success">Add Transaction</a>\r\n            <a href="/transaction/transaction.delete_all/" class="btn btn-danger">Delete All Transactions</a>\r\n          </div>\r\n        </div>\r\n      </div>\r\n<br/>\r\n      <table id="users_table" class="order-table table table-striped table-bordered">\r\n        <thead>\r\n          <th class="col-md-1">Date</th>\r\n          <th class="col-md-1">Description</th>\r\n          <th class="col-md-4">Original Description</th>\r\n          <th class="col-md-1">Amount</th>\r\n          <th class="col-md-1">Type</th>\r\n          <th class="col-md-1">Category</th>\r\n          <th class="col-md-1">Account</th>\r\n          <th class="col-md-3">Actions</th>        \r\n        </thead>\r\n')
        for trans in transaction:
            __M_writer('          <tbody>\r\n          <tr class="order-table table">\r\n            <td >')
            __M_writer(str( trans.date ))
            __M_writer('</td>\r\n            <td >')
            __M_writer(str( trans.description ))
            __M_writer('</td>\r\n            <td >')
            __M_writer(str( trans.original_description ))
            __M_writer('</td>\r\n            <td >')
            __M_writer(str( trans.amount ))
            __M_writer('</td>\r\n            <td >')
            __M_writer(str( trans.transaction_type ))
            __M_writer('</td>\r\n            <td >')
            __M_writer(str( trans.category ))
            __M_writer('</td>\r\n            <td >')
            __M_writer(str( trans.account_name ))
            __M_writer('</td>\r\n            <td >\r\n              <a href="/transaction/transaction.edit/')
            __M_writer(str( trans.id ))
            __M_writer('" class="btn btn-warning">Edit</a>\r\n              <a href="/transaction/transaction.delete/')
            __M_writer(str( trans.id ))
            __M_writer('" class="btn btn-danger">Delete</a>\r\n            </td>\r\n          </tr>\r\n          </tbody>\r\n')
        __M_writer('      </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "transaction.html", "line_map": {"128": 58, "129": 59, "130": 59, "67": 3, "73": 3, "79": 9, "131": 64, "121": 54, "85": 9, "57": 66, "137": 131, "47": 7, "28": 0, "97": 68, "91": 68, "103": 15, "42": 1, "110": 15, "111": 47, "112": 48, "113": 50, "114": 50, "115": 51, "116": 51, "117": 52, "118": 52, "119": 53, "120": 53, "52": 13, "122": 54, "123": 55, "124": 55, "125": 56, "126": 56, "127": 58}, "source_encoding": "utf-8", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\transaction\\templates/transaction.html"}
__M_END_METADATA
"""
