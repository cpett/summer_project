# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1435951826.111036
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\dashboard\\templates/dashboard.data.html'
_template_uri = 'dashboard.data.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
        trans_json = context.get('trans_json', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans_json = context.get('trans_json', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <style>\r\n\r\n.chart div {\r\n  font: 10px sans-serif;\r\n  background-color: steelblue;\r\n  text-align: right;\r\n  padding: 3px;\r\n  margin: 1px;\r\n  color: white;\r\n}\r\n\r\n</style>\r\n  <div class="content">\r\n    <h2 class="manage">Dashboard Data</h2>\r\n    <div class="clearfix"></div>\r\n    <br/>\r\n    <div class="row form-inline">\r\n      <div class="col-md-3">\r\n        <input type="search" class="light-table-filter form-control" data-table="order-table" placeholder="Filter">\r\n      </div>\r\n      <div class="col-md-3">\r\n      </div>\r\n      <div class="col-md-6">\r\n        <div class="text-right">\r\n          <button  id="button" class="btn btn-primary">Upload Instructions</button>\r\n        </div>\r\n      </div>\r\n    </div>\r\n\r\n<br/>\r\n<br/>\r\n\r\n<style>\r\n\r\nbody {\r\n  font: 10px sans-serif;\r\n}\r\n\r\n.axis path,\r\n.axis line {\r\n  fill: none;\r\n  stroke: #000;\r\n  shape-rendering: crispEdges;\r\n}\r\n\r\n.bar {\r\n  fill: orange;\r\n}\r\n\r\n.bar:hover {\r\n  fill: orangered ;\r\n}\r\n\r\n.x.axis path {\r\n  display: none;\r\n}\r\n\r\n.d3-tip {\r\n  line-height: 1;\r\n  font-weight: bold;\r\n  padding: 12px;\r\n  background: rgba(0, 0, 0, 0.8);\r\n  color: #fff;\r\n  border-radius: 2px;\r\n}\r\n\r\n/* Creates a small triangle extender for the tooltip */\r\n.d3-tip:after {\r\n  box-sizing: border-box;\r\n  display: inline;\r\n  font-size: 10px;\r\n  width: 100%;\r\n  line-height: 1;\r\n  color: rgba(0, 0, 0, 0.8);\r\n  content: "\\25BC";\r\n  position: absolute;\r\n  text-align: center;\r\n}\r\n\r\n/* Style northward tooltips differently */\r\n.d3-tip.n:after {\r\n  margin: -1px 0 0 0;\r\n  top: 100%;\r\n  left: 0;\r\n}\r\n\r\n        .axis path {\r\n            fill: none;\r\n            stroke: #777;\r\n            shape-rendering: crispEdges;\r\n        }\r\n        .axis text {\r\n            font-family: Lato;\r\n            font-size: 13px;\r\n        }\r\n</style>\r\n<body>\r\n<div class="line_chart">\r\n</div>\r\n<div class="jumbotron">\r\n            <svg id="visualisation" width="1000" height="500"></svg>\r\n</div>\r\n      <script>\r\n          function InitChart() {\r\n      /*      var data = [{\r\n                "sale": "202",\r\n                "year": "2000"\r\n            }, {\r\n                "sale": "215",\r\n                "year": "2002"\r\n            }, {\r\n                "sale": "179",\r\n                "year": "2004"\r\n            }, {\r\n                "sale": "199",\r\n                "year": "2006"\r\n            }, {\r\n                "sale": "134",\r\n                "year": "2008"\r\n            }, {\r\n                "sale": "176",\r\n                "year": "2010"\r\n            }];\r\n            var data2 = [{\r\n                "sale": "152",\r\n                "year": "2000"\r\n            }, {\r\n                "sale": "189",\r\n                "year": "2002"\r\n            }, {\r\n                "sale": "179",\r\n                "year": "2004"\r\n            }, {\r\n                "sale": "199",\r\n                "year": "2006"\r\n            }, {\r\n                "sale": "134",\r\n                "year": "2008"\r\n            }, {\r\n                "sale": "176",\r\n                "year": "2010"\r\n            }];\r\n        */\r\n        var data = ')
        __M_writer(str(trans_json))
        __M_writer('\r\n            var vis = d3.select("#visualisation"),\r\n                WIDTH = 1000,\r\n                HEIGHT = 500,\r\n                MARGINS = {\r\n                    top: 20,\r\n                    right: 20,\r\n                    bottom: 20,\r\n                    left: 50\r\n                },\r\n                xScale = d3.scale.linear().range([MARGINS.left, WIDTH - MARGINS.right]).domain([2000, 2010]),\r\n                yScale = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([134, 215]),\r\n                xAxis = d3.svg.axis()\r\n                .scale(xScale),\r\n                yAxis = d3.svg.axis()\r\n                .scale(yScale)\r\n                .orient("left");\r\n            \r\n            vis.append("svg:g")\r\n                .attr("class", "x axis")\r\n                .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")\r\n                .call(xAxis);\r\n            vis.append("svg:g")\r\n                .attr("class", "y axis")\r\n                .attr("transform", "translate(" + (MARGINS.left) + ",0)")\r\n                .call(yAxis);\r\n            var lineGen = d3.svg.line()\r\n                .x(function(d) {\r\n                    return xScale(d[0]);\r\n                })\r\n                .y(function(d) {\r\n                    return yScale(d[1]);\r\n                })\r\n                .interpolate("basis");\r\n            vis.append(\'svg:path\')\r\n                .attr(\'d\', lineGen(data))\r\n                .attr(\'stroke\', \'green\')\r\n                .attr(\'stroke-width\', 2)\r\n                .attr(\'fill\', \'none\');\r\n           /* vis.append(\'svg:path\')\r\n                .attr(\'d\', lineGen(data2))\r\n                .attr(\'stroke\', \'blue\')\r\n                .attr(\'stroke-width\', 2)\r\n                .attr(\'fill\', \'none\'); */\r\n        }\r\n        InitChart();\r\n      </script>\r\n\r\n</body>\r\n\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\dashboard\\templates/dashboard.data.html", "line_map": {"35": 1, "53": 3, "54": 147, "55": 147, "40": 199, "27": 0, "61": 55, "46": 3}, "uri": "dashboard.data.html"}
__M_END_METADATA
"""
