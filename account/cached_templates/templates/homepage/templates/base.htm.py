# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438977573.186458
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\finance/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['top', 'left', 'login', 'content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def login():
            return render_login(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    <meta name="description" content="The Colonial Heritage Foundation loves America.">\r\n    <meta name="keywords" content="colonial, heritage, liberty, America, fourth of july">\r\n    <title>Finance Something</title>\r\n    \r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\r\n    <link rel="stylesheet" href="//code.jquery.com/ui/1.11.2/themes/smoothness/jquery-ui.css">\r\n    <script src="//code.jquery.com/ui/1.11.2/jquery-ui.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/scripts/signup.js/"></script>\r\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js" charset="utf-8"></script>\r\n    <script src="http://labratrevenge.com/d3-tip/javascripts/d3.tip.v0.6.3.js"></script>\r\n    \r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n  \r\n    <style>\r\n      body {\r\n          padding-top: 70px;\r\n          /* Required padding for .navbar-fixed-top. Remove if using .navbar-static-top. Change if height of navigation changes. */\r\n      }\r\n    </style>\r\n  </head>\r\n  <body>\r\n<!-- Navigation -->\r\n    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\r\n        <div class="container">\r\n            <!-- Brand and toggle get grouped for better mobile display -->\r\n            <div class="navbar-header">\r\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n                    <span class="sr-only">Toggle navigation</span>\r\n                    <span class="icon-bar"></span>\r\n                    <span class="icon-bar"></span>\r\n                    <span class="icon-bar"></span>\r\n                </button>\r\n            </div>\r\n            <!-- Collect the nav links, forms, and other content for toggling -->\r\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n                <ul class="nav navbar-nav navar-left">\r\n')
        if request.user.is_authenticated():
            __M_writer('                    <div class="list-inline">\r\n                        <li><a href="/users/account/"><button class="btn btn-success btn-lg">My Account</button></a></li>\r\n                        <li><a href="/homepage/logout/"><button class="btn btn-primary btn-lg">Log Out</button></a></li>\r\n                    </div>\r\n')
        else:
            __M_writer('                    <div class="list-inline">\r\n                        <li><button id="show_login_dialog" class="btn btn-success btn-lg">Login</button></li>\r\n                        <li><a href="/homepage/signup.create"><button class="btn btn-primary btn-lg">Sign Up</button></a></li>\r\n                    </div>\r\n')
        __M_writer('                </ul>\r\n                \r\n                <ul class="nav navbar-nav navbar-right">\r\n')
        if request.user.is_authenticated():
            __M_writer('                    <li><a>Welcome, ')
            __M_writer(str( request.user.get_full_name() ))
            __M_writer(' </a> </li>\r\n                    \r\n                    <li>\r\n                      <a  href="/homepage/index/">Home</a>\r\n                    </li>\r\n                    <li>\r\n                        <a href="/account/account/">Accounts</a>\r\n                    </li>\r\n                    <li>\r\n                        <a href="/transaction/transaction">Transactions</a>\r\n                    </li>\r\n                    <li>\r\n                        <a href="/dashboard/dashboard">Dashboard</a>\r\n                    </li>\r\n')
        else:
            __M_writer('                        <li>\r\n                            <a href="#about">About</a>\r\n                        </li>\r\n                        <li>\r\n                            <a href="#services">Services</a>\r\n                        </li>\r\n                        <li>\r\n                            <a href="#contact">Contact</a>\r\n                        </li>\r\n')
        __M_writer('                </ul>\r\n            </div>\r\n            <!-- /.navbar-collapse -->\r\n        </div>\r\n        <!-- /.container -->\r\n    </nav>\r\n\r\n    <!-- Page Content -->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\r\n    <div class="container">\r\n        <div class="row">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </div>\r\n        <!-- /.row -->\r\n\r\n    </div>\r\n    <!-- /.container -->\r\n\r\n    <!-- jQuery Version 1.11.1 \r\n    <script src="js/jquery.js"></script>\r\n    <-->\r\n\r\n    <!-- Bootstrap Core JavaScript -->\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/bootstrap.min.js"></script>\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'login'):
            context['self'].login(**pageargs)
        

        __M_writer('\r\n      \r\n      \r\n  \r\n    <div class="wrapper">\r\n\r\n      <div class="row">\r\n\r\n      <div class="col-sm-2">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n      </div>\r\n\r\n\r\n    </div>\r\n\r\n      <div class="push"></div>\r\n\r\n    </div>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n  \r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def login():
            return render_login(context)
        __M_writer = context.writer()
        __M_writer('\r\n      <div>\r\n        <!-- Modal Login-->\r\n          <div class="modal fade" id="login_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n            <div class="modal-dialog">\r\n              <div class="modal-content">\r\n                <div class="modal-header">\r\n                  <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n                  <h4 class="modal-title" id="myModalLabel">Please Login</h4>\r\n                </div>\r\n                <div class="modal-body">\r\n                  ...\r\n                </div>\r\n                  <!--\r\n                    <div class="modal-footer">\r\n                      <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n                      <button type="button" class="btn btn-warning">Save changes</button>\r\n                    </div>\r\n                  -->\r\n              </div>\r\n            </div>\r\n          </div>\r\n        <!-- Modal Login-->\r\n          <div class="modal fade" id="instructions_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n            <div class="modal-dialog">\r\n              <div class="modal-content">\r\n                <div class="modal-header">\r\n                  <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n                  <h4 class="modal-title" id="myModalLabel">Upload Instructions</h4>\r\n                </div>\r\n                <div class="modal-body">\r\n                  Loading the CSV into the database is not a pretty process; as such, uploading your transaction history is a work-in-progress. \r\n                  <p>Currently, there is no way to check for duplicate entries, so beware when performing multiple uploads--you will need to doctor the spreadsheet first to remove duplicates. Also, the upload is a little unstable currently, especially if the user does not follow the upload steps properly. Both of these "features" will be fixed in time. <p>\r\n                  <table><tr>Steps:</tr>\r\n                  <tr>\r\n                    <li>1. Download transaction history from https://mint.com in csv format.</li>\r\n                    <li>2. Create a folder called \'temp\' on your local disk or C drive.</li>\r\n                    <li>3. Save the transactions.csv to the temp folder.</li>\r\n                    <li>4. Format the date column in the csv to follow yyyy-mm-dd.\r\n                        You can do this by highlighting the cells, right-click, select format, custom, and type yyyy-mm-dd.</li>\r\n                    <li>5. Save and exit. It is important to note that if you enter the csv file again, you will need to format the date column again.</li>\r\n                  </tr>\r\n                  </table>\r\n                </div>\r\n                  <!--\r\n                    <div class="modal-footer">\r\n                      <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n                      <button type="button" class="btn btn-warning">Save changes</button>\r\n                    </div>\r\n                  -->\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n            <div class="col-lg-12 text-center">\r\n                <h1>Lorem Ipsum</h1>\r\n                <p class="lead">Test Test Test</p>\r\n                <ul class="list-unstyled">\r\n                    <li>Bootstrap v3.3.1</li>\r\n                    <li>jQuery v1.11.1</li>\r\n                </ul>\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/homepage/templates/base.htm", "line_map": {"129": 107, "135": 107, "141": 135, "16": 4, "18": 0, "34": 2, "35": 4, "36": 5, "40": 5, "41": 16, "42": 21, "43": 21, "44": 22, "45": 22, "46": 23, "47": 23, "48": 29, "49": 29, "50": 29, "51": 54, "52": 55, "53": 59, "54": 60, "55": 65, "56": 68, "57": 69, "58": 69, "59": 69, "60": 83, "61": 84, "62": 94, "67": 104, "72": 115, "73": 128, "74": 128, "79": 184, "84": 195, "85": 206, "86": 206, "87": 206, "93": 103, "99": 103, "105": 193, "111": 193, "117": 130, "123": 130}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\finance/homepage/templates/base.htm", "source_encoding": "ascii"}
__M_END_METADATA
"""
