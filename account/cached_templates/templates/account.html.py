# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1450895573.629753
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\account\\templates/account.html'
_template_uri = 'account.html'
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
        savings = context.get('savings', UNDEFINED)
        iDebt = context.get('iDebt', UNDEFINED)
        iLongT = context.get('iLongT', UNDEFINED)
        credit_card = context.get('credit_card', UNDEFINED)
        iCash = context.get('iCash', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        checking = context.get('checking', UNDEFINED)
        other = context.get('other', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        investments = context.get('investments', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        loans = context.get('loans', UNDEFINED)
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
        savings = context.get('savings', UNDEFINED)
        iDebt = context.get('iDebt', UNDEFINED)
        iLongT = context.get('iLongT', UNDEFINED)
        credit_card = context.get('credit_card', UNDEFINED)
        iCash = context.get('iCash', UNDEFINED)
        checking = context.get('checking', UNDEFINED)
        other = context.get('other', UNDEFINED)
        def content():
            return render_content(context)
        investments = context.get('investments', UNDEFINED)
        loans = context.get('loans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Accounts</h2>\r\n      <div class="clearfix"></div>\r\n\r\n      <div class="row">\r\n        <div class="col-sm-9 col-md-10">\r\n          <h3 class="manage">Totals</h3>\r\n        </div>\r\n        <div class="col-sm-3 col-md-2">\r\n          <div class="text-right">\r\n            <a href="/account/account.create/" class="btn btn-primary">New Account</a>\r\n          </div>\r\n        </div>\r\n      </div>\r\n\r\n    <div>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n        <tr>\r\n          <th class="col-md-1">Cash</th>\r\n          <th class="col-md-1">Long Term Assets</th>\r\n          <th class="col-md-1">Debts</th>\r\n          <th class="col-md-1">Net Worth</th>\r\n          <th class="col-md-1">LT Net Worth</th>\r\n        </tr>\r\n        <tr>\r\n          <td><strong>')
        __M_writer(str( iCash ))
        __M_writer('</strong></td>\r\n          <td><strong>')
        __M_writer(str( iLongT ))
        __M_writer('</strong></td>\r\n          <td><strong>')
        __M_writer(str( iDebt ))
        __M_writer('</strong></td>\r\n          <td><strong>')
        __M_writer(str( iCash - iDebt ))
        __M_writer('</strong></td>\r\n          <td><strong>')
        __M_writer(str( iCash + iLongT - iDebt ))
        __M_writer('</strong></td>\r\n        </tr>\r\n      </table>\r\n    </div>\r\n\r\n\r\n    <div class="row">\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Checking</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-sm-1 col-md-1">Account</th>\r\n            <th class="col-sm-1 col-md-1">Ammount</th>\r\n            <th class="col-sm-1 col-md-1">Action</th>\r\n          </tr>\r\n')
        for check in checking:
            __M_writer('              <tr>\r\n                <td>')
            __M_writer(str( check.account_name ))
            __M_writer(' </td>\r\n                <td>')
            __M_writer(str( check.amount ))
            __M_writer(' </td>\r\n                <td class="text-center">\r\n                  <a href="/account/account.edit/')
            __M_writer(str( check.id ))
            __M_writer('/">Edit</a>\r\n                  |\r\n                  <a href="/account/account.delete/')
            __M_writer(str( check.id ))
            __M_writer('">Delete</a>\r\n                </td>\r\n              </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Savings</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-sm-1 col-md-1">Account</th>\r\n            <th class="col-sm-1 col-md-1">Ammount</th>\r\n            <th class="col-sm-1 col-md-1">Action</th>\r\n          </tr>\r\n')
        for saving in savings:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( saving.account_name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( saving.amount ))
            __M_writer(' </td>\r\n              <td class="text-center">\r\n                <a href="/account/account.edit/')
            __M_writer(str( saving.id ))
            __M_writer('/">Edit</a>\r\n                |\r\n                <a href="/account/account.delete/')
            __M_writer(str( saving.id ))
            __M_writer('">Delete</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Investments</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-sm-1 col-md-1">Account</th>\r\n            <th class="col-sm-1 col-md-1">Ammount</th>\r\n            <th class="col-sm-1 col-md-1">Action</th>\r\n          </tr>\r\n')
        for invest in investments:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( invest.account_name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( invest.amount ))
            __M_writer(' </td>\r\n              <td class="text-center">\r\n                <a href="/account/account.edit/')
            __M_writer(str( invest.id ))
            __M_writer('/">Edit</a>\r\n                |\r\n                <a href="/account/account.delete/')
            __M_writer(str( invest.id ))
            __M_writer('">Delete</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n    </div>\r\n\r\n    <div class="row">\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Credit Cards</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-sm-1 col-md-1">Account</th>\r\n            <th class="col-sm-1 col-md-1">Ammount</th>\r\n            <th class="col-sm-1 col-md-1">Action</th>\r\n          </tr>\r\n')
        for credit in credit_card:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( credit.account_name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( credit.amount ))
            __M_writer(' </td>\r\n              <td class="text-center">\r\n                <a href="/account/account.edit/')
            __M_writer(str( credit.id ))
            __M_writer('/">Edit</a>\r\n                |\r\n                <a href="/account/account.delete/')
            __M_writer(str( credit.id ))
            __M_writer('">Delete</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Loans</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-sm-1 col-md-1">Account</th>\r\n            <th class="col-sm-1 col-md-1">Ammount</th>\r\n            <th class="col-sm-1 col-md-1">Action</th>\r\n          </tr>\r\n')
        for loan in loans:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( loan.account_name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( loan.amount ))
            __M_writer(' </td>\r\n              <td class="text-center">\r\n                <a href="/account/account.edit/')
            __M_writer(str( loan.id ))
            __M_writer('/">Edit</a>\r\n                |\r\n                <a href="/account/account.delete/')
            __M_writer(str( loan.id ))
            __M_writer('">Delete</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Other</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-sm-1 col-md-1">Account</th>\r\n            <th class="col-sm-1 col-md-1">Ammount</th>\r\n            <th class="col-sm-1 col-md-1">Action</th>\r\n          </tr>\r\n')
        for others in other:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( others.account_name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( others.amount ))
            __M_writer(' </td>\r\n              <td class="text-center">\r\n                <a href="/account/account.edit/')
            __M_writer(str( others.id ))
            __M_writer('/">Edit</a>\r\n                |\r\n                <a href="/account/account.delete/')
            __M_writer(str( others.id ))
            __M_writer('">Delete</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "account.html", "line_map": {"28": 0, "50": 1, "55": 7, "60": 13, "65": 182, "75": 9, "81": 9, "87": 184, "93": 184, "99": 3, "105": 3, "111": 15, "126": 15, "127": 41, "128": 41, "129": 42, "130": 42, "131": 43, "132": 43, "133": 44, "134": 44, "135": 45, "136": 45, "137": 60, "138": 61, "139": 62, "140": 62, "141": 63, "142": 63, "143": 65, "144": 65, "145": 67, "146": 67, "147": 71, "148": 81, "149": 82, "150": 83, "151": 83, "152": 84, "153": 84, "154": 86, "155": 86, "156": 88, "157": 88, "158": 92, "159": 102, "160": 103, "161": 104, "162": 104, "163": 105, "164": 105, "165": 107, "166": 107, "167": 109, "168": 109, "169": 113, "170": 126, "171": 127, "172": 128, "173": 128, "174": 129, "175": 129, "176": 131, "177": 131, "178": 133, "179": 133, "180": 137, "181": 147, "182": 148, "183": 149, "184": 149, "185": 150, "186": 150, "187": 152, "188": 152, "189": 154, "190": 154, "191": 158, "192": 168, "193": 169, "194": 170, "195": 170, "196": 171, "197": 171, "198": 173, "199": 173, "200": 175, "201": 175, "202": 179, "208": 202}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\account\\templates/account.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
