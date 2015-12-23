# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1450808622.896154
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\account\\templates/account.html'
_template_uri = 'account.html'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['top', 'footer', 'content', 'header']


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
        iDebt = context.get('iDebt', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        investments = context.get('investments', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        checking = context.get('checking', UNDEFINED)
        loans = context.get('loans', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        savings = context.get('savings', UNDEFINED)
        iCash = context.get('iCash', UNDEFINED)
        iLongT = context.get('iLongT', UNDEFINED)
        credit_card = context.get('credit_card', UNDEFINED)
        other = context.get('other', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        iDebt = context.get('iDebt', UNDEFINED)
        def content():
            return render_content(context)
        investments = context.get('investments', UNDEFINED)
        checking = context.get('checking', UNDEFINED)
        loans = context.get('loans', UNDEFINED)
        savings = context.get('savings', UNDEFINED)
        credit_card = context.get('credit_card', UNDEFINED)
        iCash = context.get('iCash', UNDEFINED)
        iLongT = context.get('iLongT', UNDEFINED)
        other = context.get('other', UNDEFINED)
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
            __M_writer(' </td>\r\n                <td class="text-center">\r\n                  \r\n                    <a href="/account/account.edit/')
            __M_writer(str( check.id ))
            __M_writer('/">\r\n                      Edit\r\n                    </a>\r\n                  |\r\n                  <a href="/account/account.delete/')
            __M_writer(str( check.id ))
            __M_writer('">Delete</a>\r\n                </td>\r\n              </tr>\r\n')
        __M_writer('        </table>\r\n      </div>\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Savings</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-md-1">Account</th>\r\n            <th class="col-md-1">Ammount</th>\r\n            <th class="col-md-1">Action</th>\r\n          </tr>\r\n')
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
        __M_writer('        </table>\r\n      </div>\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Investments</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-md-1">Account</th>\r\n            <th class="col-md-1">Ammount</th>\r\n            <th class="col-md-1">Action</th>\r\n          </tr>\r\n')
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
        __M_writer('        </table>\r\n      </div>\r\n    </div>\r\n\r\n    <div class="row">\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Credit Cards</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-md-1">Account</th>\r\n            <th class="col-md-1">Ammount</th>\r\n            <th class="col-md-1">Action</th>\r\n          </tr>\r\n')
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
        __M_writer('        </table>\r\n      </div>\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Loans</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-md-1">Account</th>\r\n            <th class="col-md-1">Ammount</th>\r\n            <th class="col-md-1">Action</th>\r\n          </tr>\r\n')
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
        __M_writer('        </table>\r\n      </div>\r\n      <div class="col-md-4">\r\n        <h3 class="manage">Other</h3>\r\n        <table id="users_table" class="table table-striped table-bordered">\r\n          <tr>\r\n            <th class="col-md-1">Account</th>\r\n            <th class="col-md-1">Ammount</th>\r\n            <th class="col-md-1">Action</th>\r\n          </tr>\r\n')
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
{"line_map": {"28": 0, "50": 1, "55": 7, "60": 13, "65": 187, "75": 9, "81": 9, "87": 189, "93": 189, "99": 15, "114": 15, "115": 43, "116": 43, "117": 44, "118": 44, "119": 45, "120": 45, "121": 46, "122": 46, "123": 47, "124": 47, "125": 62, "126": 63, "127": 64, "128": 64, "129": 65, "130": 65, "131": 68, "132": 68, "133": 72, "134": 72, "135": 76, "136": 86, "137": 87, "138": 88, "139": 88, "140": 89, "141": 89, "142": 91, "143": 91, "144": 93, "145": 93, "146": 97, "147": 107, "148": 108, "149": 109, "150": 109, "151": 110, "152": 110, "153": 112, "154": 112, "155": 114, "156": 114, "157": 118, "158": 131, "159": 132, "160": 133, "161": 133, "162": 134, "163": 134, "164": 136, "165": 136, "166": 138, "167": 138, "168": 142, "169": 152, "170": 153, "171": 154, "172": 154, "173": 155, "174": 155, "175": 157, "176": 157, "177": 159, "178": 159, "179": 163, "180": 173, "181": 174, "182": 175, "183": 175, "184": 176, "185": 176, "186": 178, "187": 178, "188": 180, "189": 180, "190": 184, "196": 3, "202": 3, "208": 202}, "source_encoding": "utf-8", "uri": "account.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\account\\templates/account.html"}
__M_END_METADATA
"""
