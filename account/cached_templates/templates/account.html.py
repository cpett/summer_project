# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438977573.135455
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\account\\templates/account.html'
_template_uri = 'account.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['top', 'header', 'footer', 'content']


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
        loans = context.get('loans', UNDEFINED)
        investments = context.get('investments', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        iDebt = context.get('iDebt', UNDEFINED)
        iCash = context.get('iCash', UNDEFINED)
        iLongT = context.get('iLongT', UNDEFINED)
        checking = context.get('checking', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        other = context.get('other', UNDEFINED)
        credit_card = context.get('credit_card', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        savings = context.get('savings', UNDEFINED)
        loans = context.get('loans', UNDEFINED)
        investments = context.get('investments', UNDEFINED)
        def content():
            return render_content(context)
        iDebt = context.get('iDebt', UNDEFINED)
        iCash = context.get('iCash', UNDEFINED)
        iLongT = context.get('iLongT', UNDEFINED)
        checking = context.get('checking', UNDEFINED)
        other = context.get('other', UNDEFINED)
        credit_card = context.get('credit_card', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"uri": "account.html", "line_map": {"27": 0, "49": 1, "54": 7, "59": 13, "64": 184, "74": 9, "80": 9, "86": 3, "92": 3, "98": 186, "104": 186, "110": 15, "125": 15, "126": 43, "127": 43, "128": 44, "129": 44, "130": 45, "131": 45, "132": 46, "133": 46, "134": 47, "135": 47, "136": 62, "137": 63, "138": 64, "139": 64, "140": 65, "141": 65, "142": 67, "143": 67, "144": 69, "145": 69, "146": 73, "147": 83, "148": 84, "149": 85, "150": 85, "151": 86, "152": 86, "153": 88, "154": 88, "155": 90, "156": 90, "157": 94, "158": 104, "159": 105, "160": 106, "161": 106, "162": 107, "163": 107, "164": 109, "165": 109, "166": 111, "167": 111, "168": 115, "169": 128, "170": 129, "171": 130, "172": 130, "173": 131, "174": 131, "175": 133, "176": 133, "177": 135, "178": 135, "179": 139, "180": 149, "181": 150, "182": 151, "183": 151, "184": 152, "185": 152, "186": 154, "187": 154, "188": 156, "189": 156, "190": 160, "191": 170, "192": 171, "193": 172, "194": 172, "195": 173, "196": 173, "197": 175, "198": 175, "199": 177, "200": 177, "201": 181, "207": 201}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\account\\templates/account.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
