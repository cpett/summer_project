# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1443755567.031441
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\account\\templates/account.html'
_template_uri = 'account.html'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['header', 'content', 'footer', 'top']


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
        def content():
            return render_content(context._locals(__M_locals))
        loans = context.get('loans', UNDEFINED)
        checking = context.get('checking', UNDEFINED)
        iLongT = context.get('iLongT', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        savings = context.get('savings', UNDEFINED)
        other = context.get('other', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        investments = context.get('investments', UNDEFINED)
        iDebt = context.get('iDebt', UNDEFINED)
        credit_card = context.get('credit_card', UNDEFINED)
        iCash = context.get('iCash', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        loans = context.get('loans', UNDEFINED)
        checking = context.get('checking', UNDEFINED)
        iLongT = context.get('iLongT', UNDEFINED)
        savings = context.get('savings', UNDEFINED)
        other = context.get('other', UNDEFINED)
        investments = context.get('investments', UNDEFINED)
        iDebt = context.get('iDebt', UNDEFINED)
        credit_card = context.get('credit_card', UNDEFINED)
        iCash = context.get('iCash', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "account.html", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\summer_project\\account\\templates/account.html", "line_map": {"28": 0, "50": 1, "55": 7, "60": 13, "65": 184, "75": 3, "81": 3, "87": 15, "102": 15, "103": 43, "104": 43, "105": 44, "106": 44, "107": 45, "108": 45, "109": 46, "110": 46, "111": 47, "112": 47, "113": 62, "114": 63, "115": 64, "116": 64, "117": 65, "118": 65, "119": 67, "120": 67, "121": 69, "122": 69, "123": 73, "124": 83, "125": 84, "126": 85, "127": 85, "128": 86, "129": 86, "130": 88, "131": 88, "132": 90, "133": 90, "134": 94, "135": 104, "136": 105, "137": 106, "138": 106, "139": 107, "140": 107, "141": 109, "142": 109, "143": 111, "144": 111, "145": 115, "146": 128, "147": 129, "148": 130, "149": 130, "150": 131, "151": 131, "152": 133, "153": 133, "154": 135, "155": 135, "156": 139, "157": 149, "158": 150, "159": 151, "160": 151, "161": 152, "162": 152, "163": 154, "164": 154, "165": 156, "166": 156, "167": 160, "168": 170, "169": 171, "170": 172, "171": 172, "172": 173, "173": 173, "174": 175, "175": 175, "176": 177, "177": 177, "178": 181, "184": 186, "190": 186, "196": 9, "202": 9, "208": 202}}
__M_END_METADATA
"""
