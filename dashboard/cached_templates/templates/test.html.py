# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438039007.872624
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\dashboard\\templates/test.html'
_template_uri = 'test.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE HTML>\r\n<meta charset="utf-8">\r\n<html>\r\n<style>\r\n\r\nbody {\r\n  font: 10px sans-serif;\r\n}\r\n\r\ndiv {\r\n  padding-left: 100px;\r\n  padding-top: 10px;\r\n  width: 30%;\r\n  margin: 0 auto;\r\n  font: 14px;\r\n}\r\n\r\ninput {\r\n  border-top: 0;\r\n  border-left: 0;\r\n  border-right: 0;\r\n  text-align: center;\r\n  font: 14px;\r\n  width: 60px;\r\n}\r\n</style>\r\n\r\n<body>\r\n  <div>\r\n  </div>\r\n      <div class="pie_chart">\r\n    </div>\r\n<script src="http://d3js.org/d3.v3.min.js"></script>\r\n<script>\r\nvar width = 960,\r\n    height = 500 - 29; // adjust for height of input bar div\r\n\r\nvar color = d3.scale.category20();\r\n\r\n// draw and append the container\r\nvar svg = d3.select(".pie_chart").append("svg")\r\n  .attr("width", width).attr("height", height);\r\n\r\n// set the thickness of the inner and outer radii\r\nvar min = Math.min(width, height);\r\nvar oRadius = min / 2 * 0.9;\r\nvar iRadius = min / 2 * 0.85;\r\n\r\n// construct default pie laoyut\r\nvar pie = d3.layout.pie().value(function(d){ return d; }).sort(null);\r\n\r\n// construct arc generator\r\nvar arc = d3.svg.arc()\r\n  .outerRadius(oRadius)\r\n  .innerRadius(iRadius);\r\n\r\n// creates the pie chart container\r\nvar g = svg.append(\'g\')\r\nvar g = svg.append(\'g\')\r\n  .attr(\'transform\', function(){\r\n    if ( window.innerWidth >= 960 ) var shiftWidth = width / 2;\r\n    if ( window.innerWidth < 960 ) var shiftWidth = width / 3;\r\n    return \'translate(\' + shiftWidth + \',\' + height / 2 + \')\';\r\n  })\r\n\r\n// generate random data\r\nvar data = makeData(+15);\r\n\r\n// enter data and draw pie chart\r\nvar path = g.datum(data).selectAll("path")\r\n  .data(pie)\r\n  .enter().append("path")\r\n    .attr("class","piechart")\r\n    .attr("fill", function(d,i){ return color(i); })\r\n    .attr("d", arc)\r\n    .each(function(d){ this._current = d; })\r\n\r\nfunction render(){\r\n  // generate new random data\r\n  data = makeData(+document.getElementById("datacount").value);\r\n  // add transition to new path\r\n  g.datum(data).selectAll("path").data(pie).transition().duration(1000).attrTween("d", arcTween)\r\n\r\n  // add any new paths\r\n  g.datum(data).selectAll("path")\r\n    .data(pie)\r\n  .enter().append("path")\r\n    .attr("class","piechart")\r\n    .attr("fill", function(d,i){ return color(i); })\r\n    .attr("d", arc)\r\n    .each(function(d){ this._current = d; })\r\n\r\n  // remove data not being used\r\n  g.datum(data).selectAll("path")\r\n    .data(pie).exit().remove();\r\n}\r\n\r\nrender();\r\nsetInterval(render,2000);\r\n\r\nfunction makeData(size){\r\n  return d3.range(size).map(function(item){\r\n   return Math.random()*100;\r\n  });\r\n};\r\n\r\n// Store the displayed angles in _current.\r\n// Then, interpolate from _current to the new angles.\r\n// During the transition, _current is updated in-place by d3.interpolate.\r\nfunction arcTween(a) {\r\n  var i = d3.interpolate(this._current, a);\r\n  this._current = i(0);\r\n  return function(t) {\r\n    return arc(i(t));\r\n  };\r\n}\r\n</script>\r\n</body>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\dashboard\\templates/test.html", "line_map": {"16": 0, "27": 21, "21": 1}, "source_encoding": "ascii", "uri": "test.html"}
__M_END_METADATA
"""
