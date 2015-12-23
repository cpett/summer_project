# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1450804131.5728366
_enable_loop = True
_template_filename = 'homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import os, os.path, re
_exports = ['login', 'top', 'left', 'content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def login():
            return render_login(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    <meta name="description" content="The Colonial Heritage Foundation loves America.">\n    <meta name="keywords" content="colonial, heritage, liberty, America, fourth of july">\n    <title>Finance Something</title>\n    \n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n    <link rel="stylesheet" href="//code.jquery.com/ui/1.11.2/themes/smoothness/jquery-ui.css">\n    <script src="//code.jquery.com/ui/1.11.2/jquery-ui.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/scripts/signup.js/"></script>\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js" charset="utf-8"></script>\n    <script src="http://labratrevenge.com/d3-tip/javascripts/d3.tip.v0.6.3.js"></script>\n    \n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n    <style>\n      body {\n          padding-top: 70px;\n          /* Required padding for .navbar-fixed-top. Remove if using .navbar-static-top. Change if height of navigation changes. */\n      }\n    </style>\n  </head>\n  <body>\n<!-- Navigation -->\n    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n        <div class="container">\n            <!-- Brand and toggle get grouped for better mobile display -->\n            <div class="navbar-header">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>\n            </div>\n            <!-- Collect the nav links, forms, and other content for toggling -->\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n                <ul class="nav navbar-nav navar-left">\n')
        if request.user.is_authenticated():
            __M_writer('                    <div class="list-inline">\n                        <li><a href="/users/account/"><button class="btn btn-success btn-lg">My Account</button></a></li>\n                        <li><a href="/homepage/logout/"><button class="btn btn-primary btn-lg">Log Out</button></a></li>\n                    </div>\n')
        else:
            __M_writer('                    <div class="list-inline">\n                        <li><button id="show_login_dialog" class="btn btn-success btn-lg">Login</button></li>\n                        <li><a href="/homepage/signup.create"><button class="btn btn-primary btn-lg">Sign Up</button></a></li>\n                    </div>\n')
        __M_writer('                </ul>\n                \n                <ul class="nav navbar-nav navbar-right">\n')
        if request.user.is_authenticated():
            __M_writer('                    <li><a>Welcome, ')
            __M_writer(str( request.user.get_full_name() ))
            __M_writer(' </a> </li>\n                    \n                    <li>\n                      <a  href="/homepage/index/">Home</a>\n                    </li>\n                    <li>\n                        <a href="/account/account/">Accounts</a>\n                    </li>\n                    <li>\n                        <a href="/transaction/transaction">Transactions</a>\n                    </li>\n                    <li>\n                        <a href="/dashboard/dashboard">Dashboard</a>\n                    </li>\n')
        else:
            __M_writer('                        <li>\n                            <a href="#about">About</a>\n                        </li>\n                        <li>\n                            <a href="#services">Services</a>\n                        </li>\n                        <li>\n                            <a href="#contact">Contact</a>\n                        </li>\n')
        __M_writer('                </ul>\n            </div>\n            <!-- /.navbar-collapse -->\n        </div>\n        <!-- /.container -->\n    </nav>\n\n    <!-- Page Content -->\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\n    <div class="container">\n        <div class="row">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n            </div>\n        </div>\n        <!-- /.row -->\n\n    </div>\n    <!-- /.container -->\n\n    <!-- jQuery Version 1.11.1 \n    <script src="js/jquery.js"></script>\n    <-->\n\n    <!-- Bootstrap Core JavaScript -->\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/bootstrap.min.js"></script>\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'login'):
            context['self'].login(**pageargs)
        

        __M_writer('\n      \n      \n  \n    <div class="wrapper">\n\n      <div class="row">\n\n      <div class="col-sm-2">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n      </div>\n\n\n    </div>\n\n      <div class="push"></div>\n\n    </div>\n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def login():
            return render_login(context)
        __M_writer = context.writer()
        __M_writer('\n      <div>\n        <!-- Modal Login-->\n          <div class="modal fade" id="login_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n            <div class="modal-dialog">\n              <div class="modal-content">\n                <div class="modal-header">\n                  <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n                  <h4 class="modal-title" id="myModalLabel">Please Login</h4>\n                </div>\n                <div class="modal-body">\n                  ...\n                </div>\n                  <!--\n                    <div class="modal-footer">\n                      <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                      <button type="button" class="btn btn-warning">Save changes</button>\n                    </div>\n                  -->\n              </div>\n            </div>\n          </div>\n        <!-- Modal Login-->\n          <div class="modal fade" id="instructions_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n            <div class="modal-dialog">\n              <div class="modal-content">\n                <div class="modal-header">\n                  <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n                  <h4 class="modal-title" id="myModalLabel">Upload Instructions</h4>\n                </div>\n                <div class="modal-body">\n                  Loading the CSV into the database is not a pretty process; as such, uploading your transaction history is a work-in-progress. \n                  <p>Currently, there is no way to check for duplicate entries, so beware when performing multiple uploads--you will need to doctor the spreadsheet first to remove duplicates. Also, the upload is a little unstable currently, especially if the user does not follow the upload steps properly. Both of these "features" will be fixed in time. <p>\n                  <table><tr>Steps:</tr>\n                  <tr>\n                    <li>1. Download transaction history from https://mint.com in csv format.</li>\n                    <li>2. Create a folder called \'temp\' on your local disk or C drive.</li>\n                    <li>3. Save the transactions.csv to the temp folder.</li>\n                    <li>4. Format the date column in the csv to follow yyyy-mm-dd.\n                        You can do this by highlighting the cells, right-click, select format, custom, and type yyyy-mm-dd.</li>\n                    <li>5. Save and exit. It is important to note that if you enter the csv file again, you will need to format the date column again.</li>\n                  </tr>\n                  </table>\n                </div>\n                  <!--\n                    <div class="modal-footer">\n                      <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                      <button type="button" class="btn btn-warning">Save changes</button>\n                    </div>\n                  -->\n              </div>\n            </div>\n          </div>\n        </div>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n            <div class="col-lg-12 text-center">\n                <h1>Lorem Ipsum</h1>\n                <p class="lead">Test Test Test</p>\n                <ul class="list-unstyled">\n                    <li>Bootstrap v3.3.1</li>\n                    <li>jQuery v1.11.1</li>\n                </ul>\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/homepage/templates/base.htm", "line_map": {"130": 107, "136": 107, "142": 136, "17": 4, "19": 0, "35": 2, "36": 4, "37": 5, "41": 5, "42": 16, "43": 21, "44": 21, "45": 22, "46": 22, "47": 23, "48": 23, "49": 29, "50": 29, "51": 29, "52": 54, "53": 55, "54": 59, "55": 60, "56": 65, "57": 68, "58": 69, "59": 69, "60": 69, "61": 83, "62": 84, "63": 94, "68": 104, "73": 115, "74": 128, "75": 128, "80": 184, "85": 195, "86": 206, "87": 206, "88": 206, "94": 130, "100": 130, "106": 103, "112": 103, "118": 193, "124": 193}, "filename": "homepage/templates/base.htm", "source_encoding": "utf-8"}
__M_END_METADATA
"""
