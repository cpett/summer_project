# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1450892098.2350533
_enable_loop = True
_template_filename = '/home/cpett/summer_project/transaction/templates/transaction.html'
_template_uri = 'transaction.html'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['footer', 'top', 'header', 'content']


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
        transaction = context.get('transaction', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

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
        __M_writer('\n    <div class="header">\n\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        transaction = context.get('transaction', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n      <h2 class="manage">Transaction Index</h2>\n      <div class="clearfix"></div>\n      <br/>\n      <div class="row form-inline">\n        <div class="col-md-3">\n          <input type="search" class="light-table-filter form-control" data-table="order-table" placeholder="Filter">\n        </div>\n        <div class="col-md-3">\n        </div>\n        <div class="col-md-6">\n          <div class="text-right">\n            <button  id="show_instructions_dialog" class="btn btn-primary">Upload Instructions</button>\n            <a href="/transaction/transaction.upload/" class="btn btn-success">Upload CSV</a>\n            <a href="/transaction/transaction.create/" class="btn btn-warning">Add Transaction</a>\n            <a href="/transaction/transaction.delete_all/" class="btn btn-danger">Delete All Transactions</a>\n          </div>\n        </div>\n      </div>\n<br/>\n      <table id="users_table" class="order-table table table-striped table-bordered">\n        <thead>\n          <th class="col-sm-1 col-md-1">Date</th>\n          <th class="col-sm-1 col-md-1">Description</th>\n          <th class="col-sm-5 col-md-5">Original Description</th>\n          <th class="col-sm-1 col-md-1">Amount</th>\n          <th class="col-sm-1 col-md-1">Type</th>\n          <th class="col-sm-1 col-md-1">Category</th>\n          <th class="col-sm-1 col-md-1">Account</th>\n          <th class="col-sm-2 col-md-2">Actions</th>        \n        </thead>\n')
        for trans in transaction:
            __M_writer('          <tbody>\n          <tr class="order-table table">\n            <td >')
            __M_writer(str( trans.date ))
            __M_writer('</td>\n            <td >')
            __M_writer(str( trans.description ))
            __M_writer('</td>\n            <td >')
            __M_writer(str( trans.original_description ))
            __M_writer('</td>\n            <td >')
            __M_writer(str( trans.amount ))
            __M_writer('</td>\n            <td >')
            __M_writer(str( trans.transaction_type ))
            __M_writer('</td>\n            <td >')
            __M_writer(str( trans.category ))
            __M_writer('</td>\n            <td >')
            __M_writer(str( trans.account_name ))
            __M_writer('</td>\n\t    <td class="text-center">\n              <a href="/transaction/transaction.edit/')
            __M_writer(str( trans.id ))
            __M_writer('" class="btn btn-info btn-sm"\n                data-toggle="tooltip" data-placement="bottom" title="Edit">\n                <span class="glyphicon glyphicon-edit" aria-hidden="true"></span>\n              </a>\n              <a href="/transaction/transaction.delete/')
            __M_writer(str( trans.id ))
            __M_writer('" class="btn btn-danger btn-sm"\n                data-toggle="tooltip" data-placement="bottom" title="Remove">\n               <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>\n              </a>\n            </td>\n          </tr>\n          </tbody>\n')
        __M_writer('      </table>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "transaction.html", "line_map": {"128": 58, "129": 58, "130": 62, "131": 62, "68": 74, "74": 74, "126": 56, "138": 132, "80": 9, "121": 53, "86": 9, "57": 72, "132": 70, "111": 15, "28": 0, "98": 3, "104": 15, "92": 3, "42": 1, "47": 7, "112": 47, "113": 48, "114": 50, "115": 50, "116": 51, "117": 51, "118": 52, "119": 52, "120": 53, "52": 13, "122": 54, "123": 54, "124": 55, "125": 55, "62": 77, "127": 56}, "filename": "/home/cpett/summer_project/transaction/templates/transaction.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
