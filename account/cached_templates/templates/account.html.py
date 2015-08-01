# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1437611064.705312
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\account\\templates/account.html'
_template_uri = 'account.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footer', 'top', 'content', 'header']


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
        def header():
            return render_header(context._locals(__M_locals))
        iDebt = context.get('iDebt', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        loans = context.get('loans', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        iCash = context.get('iCash', UNDEFINED)
        other = context.get('other', UNDEFINED)
        checking = context.get('checking', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        iLongT = context.get('iLongT', UNDEFINED)
        credit_card = context.get('credit_card', UNDEFINED)
        investments = context.get('investments', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        savings = context.get('savings', UNDEFINED)
        iDebt = context.get('iDebt', UNDEFINED)
        loans = context.get('loans', UNDEFINED)
        iCash = context.get('iCash', UNDEFINED)
        other = context.get('other', UNDEFINED)
        checking = context.get('checking', UNDEFINED)
        def content():
            return render_content(context)
        iLongT = context.get('iLongT', UNDEFINED)
        credit_card = context.get('credit_card', UNDEFINED)
        investments = context.get('investments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h2 class="manage">Accounts</h2>\r\n      <div class="clearfix"></div>\r\n\r\n      <div class="row">\r\n        <div class="col-md-1">\r\n          <h3 class="manage">Totals</h3>\r\n        </div>\r\n        <div class="col-md-9">\r\n        </div>\r\n        <div class="col-md-2">\r\n          <div class="text-right">\r\n            <a href="/account/account.create/" class="btn btn-primary">Create New Account</a>\r\n          </div>\r\n        </div>\r\n      </div>\r\n\r\n    <div>\r\n      <table id="users_table" class="table table-striped table-bordered">\r\n        <tr>\r\n          <th class="col-md-1">Cash</th>\r\n          <th class="col-md-1">Long Term Assets</th>\r\n          <th class="col-md-1">Debts</th>\r\n          <th class="col-md-1">Net Worth</th>\r\n          <th class="col-md-1">LT Net Worth</th>\r\n        </tr>\r\n        <tr>\r\n          <td><strong>')
        __M_writer(str( iCash ))
        __M_writer('</strong></td>\r\n          <td><strong>')
        __M_writer(str( iLongT ))
        __M_writer('</strong></td>\r\n          <td><strong>')
        __M_writer(str( iDebt ))
        __M_writer('</strong></td>\r\n          <td><strong>')
        __M_writer(str( iCash - iDebt ))
        __M_writer('</strong></td>\r\n          <td><strong>')
        __M_writer(str( iCash + iLongT - iDebt ))
        __M_writer('</strong></td>\r\n        </tr>\r\n      </table>\r\n    </div>\r\n\r\n\r\n    <div class="row">\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Checking</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-md-1">Account</th>\r\n            <th class="col-md-1">Ammount</th>\r\n            <th class="col-md-1">Action</th>\r\n          </tr>\r\n')
        for check in checking:
            __M_writer('              <tr>\r\n                <td>')
            __M_writer(str( check.account_name ))
            __M_writer(' </td>\r\n                <td>')
            __M_writer(str( check.amount ))
            __M_writer(' </td>\r\n                <td>\r\n                  <a href="/account/account.edit/')
            __M_writer(str( check.id ))
            __M_writer('/">Edit</a>\r\n                  |\r\n                  <a href="/account/account.delete/')
            __M_writer(str( check.id ))
            __M_writer('">Delete</a>\r\n                </td>\r\n              </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Savings</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-md-1">Account</th>\r\n            <th class="col-md-1">Ammount</th>\r\n            <th class="col-md-1">Action</th>\r\n          </tr>\r\n')
        for saving in savings:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( saving.account_name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( saving.amount ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/account/account.edit/')
            __M_writer(str( saving.id ))
            __M_writer('/">Edit</a>\r\n                |\r\n                <a href="/account/account.delete/')
            __M_writer(str( saving.id ))
            __M_writer('">Delete</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Investments</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-md-1">Account</th>\r\n            <th class="col-md-1">Ammount</th>\r\n            <th class="col-md-1">Action</th>\r\n          </tr>\r\n')
        for invest in investments:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( invest.account_name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( invest.amount ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/account/account.edit/')
            __M_writer(str( invest.id ))
            __M_writer('/">Edit</a>\r\n                |\r\n                <a href="/account/account.delete/')
            __M_writer(str( invest.id ))
            __M_writer('">Delete</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n    </div>\r\n\r\n    <div class="row">\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Credit Cards</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-md-1">Account</th>\r\n            <th class="col-md-1">Ammount</th>\r\n            <th class="col-md-1">Action</th>\r\n          </tr>\r\n')
        for credit in credit_card:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( credit.account_name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( credit.amount ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/account/account.edit/')
            __M_writer(str( credit.id ))
            __M_writer('/">Edit</a>\r\n                |\r\n                <a href="/account/account.delete/')
            __M_writer(str( credit.id ))
            __M_writer('">Delete</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Loans</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-md-1">Account</th>\r\n            <th class="col-md-1">Ammount</th>\r\n            <th class="col-md-1">Action</th>\r\n          </tr>\r\n')
        for loan in loans:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( loan.account_name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( loan.amount ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/account/account.edit/')
            __M_writer(str( loan.id ))
            __M_writer('/">Edit</a>\r\n                |\r\n                <a href="/account/account.delete/')
            __M_writer(str( loan.id ))
            __M_writer('">Delete</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Other</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-md-1">Account</th>\r\n            <th class="col-md-1">Ammount</th>\r\n            <th class="col-md-1">Action</th>\r\n          </tr>\r\n')
        for others in other:
            __M_writer('            <tr>\r\n              <td>')
            __M_writer(str( others.account_name ))
            __M_writer(' </td>\r\n              <td>')
            __M_writer(str( others.amount ))
            __M_writer(' </td>\r\n              <td>\r\n                <a href="/account/account.edit/')
            __M_writer(str( others.id ))
            __M_writer('/">Edit</a>\r\n                |\r\n                <a href="/account/account.delete/')
            __M_writer(str( others.id ))
            __M_writer('">Delete</a>\r\n              </td>\r\n            </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n    </div>\r\n')
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


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\account\\templates/account.html", "uri": "account.html", "line_map": {"27": 0, "49": 1, "54": 7, "59": 13, "64": 184, "74": 186, "80": 186, "86": 9, "92": 9, "98": 15, "113": 15, "114": 43, "115": 43, "116": 44, "117": 44, "118": 45, "119": 45, "120": 46, "121": 46, "122": 47, "123": 47, "124": 62, "125": 63, "126": 64, "127": 64, "128": 65, "129": 65, "130": 67, "131": 67, "132": 69, "133": 69, "134": 73, "135": 83, "136": 84, "137": 85, "138": 85, "139": 86, "140": 86, "141": 88, "142": 88, "143": 90, "144": 90, "145": 94, "146": 104, "147": 105, "148": 106, "149": 106, "150": 107, "151": 107, "152": 109, "153": 109, "154": 111, "155": 111, "156": 115, "157": 128, "158": 129, "159": 130, "160": 130, "161": 131, "162": 131, "163": 133, "164": 133, "165": 135, "166": 135, "167": 139, "168": 149, "169": 150, "170": 151, "171": 151, "172": 152, "173": 152, "174": 154, "175": 154, "176": 156, "177": 156, "178": 160, "179": 170, "180": 171, "181": 172, "182": 172, "183": 173, "184": 173, "185": 175, "186": 175, "187": 177, "188": 177, "189": 181, "195": 3, "201": 3, "207": 201}}
__M_END_METADATA
"""
