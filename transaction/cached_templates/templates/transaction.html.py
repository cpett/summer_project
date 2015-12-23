# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1450895588.873198
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\transaction\\templates/transaction.html'
_template_uri = 'transaction.html'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['top', 'footer', 'header', 'content']


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
        def footer():
            return render_footer(context._locals(__M_locals))
        transaction = context.get('transaction', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        transaction = context.get('transaction', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Transaction Index</h2>\r\n      <div class="clearfix"></div>\r\n      <br/>\r\n      <div class="row form-inline">\r\n        <div class="col-sm-6 col-md-6">\r\n          <input type="search" class="light-table-filter form-control" data-table="order-table" placeholder="Filter">\r\n        </div>\r\n        <div class="col-sm-6 col-md-6">\r\n          <div class="dropdown text-right">\r\n            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">\r\n              Actions\r\n              <span class="caret"></span>\r\n            </button>\r\n            <ul class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenu1">\r\n              <li><a href="/transaction/transaction.upload/">Upload CSV</a></li>\r\n              <li><a href="/transaction/transaction.create/">Add Transaction</a></li>\r\n              <li><a href="/transaction/transaction.delete_all/">Delete All Transactions</a></li>\r\n            </ul>\r\n          </div>\r\n        </div>\r\n      </div>\r\n<br/>\r\n      <table id="users_table" class="order-table table table-striped table-bordered">\r\n        <thead>\r\n          <th class="col-sm-2 col-md-2">Date</th>\r\n          <th class="col-sm-1 col-md-1">Description</th>\r\n          <th class="col-sm-4 col-md-4">Original Description</th>\r\n          <th class="col-sm-1 col-md-1">Amount</th>\r\n          <th class="col-sm-1 col-md-1">Type</th>\r\n          <th class="col-sm-1 col-md-1">Category</th>\r\n          <th class="col-sm-1 col-md-1">Account</th>\r\n          <th class="col-sm-2 col-md-2">Actions</th>        \r\n        </thead>\r\n')
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
            __M_writer('</td>\r\n\t    <td class="text-center">\r\n              <a href="/transaction/transaction.edit/')
            __M_writer(str( trans.id ))
            __M_writer('" class="btn btn-info btn-sm"\r\n                data-toggle="tooltip" data-placement="bottom" title="Edit">\r\n                <span class="glyphicon glyphicon-edit" aria-hidden="true"></span>\r\n              </a>\r\n              <a href="/transaction/transaction.delete/')
            __M_writer(str( trans.id ))
            __M_writer('" class="btn btn-danger btn-sm"\r\n                data-toggle="tooltip" data-placement="bottom" title="Remove">\r\n               <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>\r\n              </a>\r\n            </td>\r\n          </tr>\r\n          </tbody>\r\n')
        __M_writer('      </table>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "transaction.html", "line_map": {"128": 61, "129": 61, "130": 65, "131": 65, "68": 9, "74": 9, "126": 59, "138": 132, "80": 77, "121": 56, "86": 77, "57": 75, "132": 73, "111": 15, "28": 0, "98": 3, "104": 15, "92": 3, "42": 1, "47": 7, "112": 50, "113": 51, "114": 53, "115": 53, "116": 54, "117": 54, "118": 55, "119": 55, "120": 56, "52": 13, "122": 57, "123": 57, "124": 58, "125": 58, "62": 80, "127": 59}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\transaction\\templates/transaction.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
