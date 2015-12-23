# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1450884087.514454
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\transaction\\templates/transaction.html'
_template_uri = 'transaction.html'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['content', 'top', 'header', 'footer']


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
        pages = context.get('pages', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        previous_page = context.get('previous_page', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        next_page = context.get('next_page', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        transaction = context.get('transaction', UNDEFINED)
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
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        pages = context.get('pages', UNDEFINED)
        next_page = context.get('next_page', UNDEFINED)
        previous_page = context.get('previous_page', UNDEFINED)
        transaction = context.get('transaction', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Transaction Index</h2>\r\n      <div class="clearfix"></div>\r\n      <br/>\r\n      <div class="row form-inline">\r\n        <div class="col-md-3">\r\n          <input type="search" class="light-table-filter form-control" data-table="order-table" placeholder="Filter">\r\n        </div>\r\n        <div class="col-md-3">\r\n        </div>\r\n        <div class="col-md-6">\r\n          <div class="text-right">\r\n            <button  id="show_instructions_dialog" class="btn btn-primary">Upload Instructions</button>\r\n            <a href="/transaction/transaction.upload/" class="btn btn-success">Upload CSV</a>\r\n            <a href="/transaction/transaction.create/" class="btn btn-warning">Add Transaction</a>\r\n            <a href="/transaction/transaction.delete_all/" class="btn btn-danger">Delete All Transactions</a>\r\n          </div>\r\n        </div>\r\n      </div>\r\n<br/>\r\n      <table id="users_table" class="order-table table table-striped table-bordered">\r\n        <thead>\r\n          <th class="col-md-1">Date</th>\r\n          <th class="col-md-1">Description</th>\r\n          <th class="col-md-5">Original Description</th>\r\n          <th class="col-md-1">Amount</th>\r\n          <th class="col-md-1">Type</th>\r\n          <th class="col-md-1">Category</th>\r\n          <th class="col-md-1">Account</th>\r\n          <th class="col-md-2">Actions</th>        \r\n        </thead>\r\n')
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
            __M_writer('</td>\r\n            <td class="text-center">\r\n              <a href="/transaction/transaction.edit/')
            __M_writer(str( trans.id ))
            __M_writer('" class="btn btn-info btn-sm"\r\n                data-toggle="tooltip" data-placement="bottom" title="Edit">\r\n                <span class="glyphicon glyphicon-edit" aria-hidden="true"></span>\r\n              </a>\r\n              <a href="/transaction/transaction.delete/')
            __M_writer(str( trans.id ))
            __M_writer('" class="btn btn-danger btn-sm"\r\n                data-toggle="tooltip" data-placement="bottom" title="Remove">\r\n                <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>\r\n              </a>\r\n            </td>\r\n          </tr>\r\n          </tbody>\r\n')
        __M_writer('      </table>\r\n    </div>\r\n<!--PAGINATION-->\r\n    <div class="col-sm-12 col-md-12 col-lg-12 text-center">\r\n      <ul class="pagination">\r\n')
        if transaction.number > 1:
            __M_writer('          <li>\r\n            <a href="?page=')
            __M_writer(str( previous_page ))
            __M_writer('" aria-label="Previous">\r\n              <span aria-hidden="true">&laquo;</span>\r\n            </a>\r\n          </li>\r\n')
        for page in pages:
            __M_writer('          <li><a href="?page=')
            __M_writer(str( page ))
            __M_writer('">')
            __M_writer(str( page ))
            __M_writer('</a></li>\r\n')
        if next_page <= transaction.paginator.num_pages:
            __M_writer('          <li>\r\n            <a href="?page=')
            __M_writer(str( next_page ))
            __M_writer('" aria-label="Next">\r\n              <span aria-hidden="true">&raquo;</span>\r\n            </a>\r\n          </li>\r\n')
        __M_writer('      </ul>\r\n    </div>\r\n    <div class="text-center">\r\n      Page ')
        __M_writer(str( transaction.number ))
        __M_writer(' of ')
        __M_writer(str( transaction.paginator.num_pages ))
        __M_writer('\r\n    </div>\r\n')
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
        __M_writer('\r\n    <div class="header">\r\n\r\n    </div>\r\n')
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


"""
__M_BEGIN_METADATA
{"line_map": {"132": 9, "138": 3, "144": 3, "150": 99, "28": 0, "162": 156, "156": 99, "45": 1, "50": 7, "55": 13, "60": 97, "70": 15, "80": 15, "81": 47, "82": 48, "83": 50, "84": 50, "85": 51, "86": 51, "87": 52, "88": 52, "89": 53, "90": 53, "91": 54, "92": 54, "93": 55, "94": 55, "95": 56, "96": 56, "97": 58, "98": 58, "99": 62, "100": 62, "101": 70, "102": 75, "103": 76, "104": 77, "105": 77, "106": 82, "107": 83, "108": 83, "109": 83, "110": 83, "111": 83, "112": 85, "113": 86, "114": 87, "115": 87, "116": 92, "117": 95, "118": 95, "119": 95, "120": 95, "126": 9}, "source_encoding": "utf-8", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\transaction\\templates/transaction.html", "uri": "transaction.html"}
__M_END_METADATA
"""
