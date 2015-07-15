# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1436916402.922922
_enable_loop = True
_template_filename = 'C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\dashboard\\templates/dashboard.html'
_template_uri = 'dashboard.html'
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
        dc_json = context.get('dc_json', UNDEFINED)
        types_json = context.get('types_json', UNDEFINED)
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
        dc_json = context.get('dc_json', UNDEFINED)
        types_json = context.get('types_json', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="content">\r\n    <h2 class="manage">Dashboard</h2>\r\n    <div class="clearfix"></div>\r\n    <br/>\r\n    <div class="row form-inline">\r\n      <div class="col-md-3">\r\n        <h3>Accounts Overview</h3>\r\n        <select id="d_list" onChange="updateData()">\r\n            <option value="All">All</option>\r\n            <option value="Checking">Checking</option>\r\n            <option value="Credit Card">Credit Card</option>\r\n            <option value="Investments">Investments</option>\r\n            <option value="Savings">Savings</option>\r\n            <option value="Other">Other</option>\r\n        </select>\r\n      </div>\r\n      <div class="col-md-3">\r\n      </div>\r\n      <div class="col-md-3">\r\n        <div class="text-right">\r\n          <h3>Lorem Ipsum</h3>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n  <div class="row form-inline">\r\n    <div class="col-md-6">\r\n      <div class="bar_chart">\r\n      </div>\r\n    </div>\r\n    <div class="col-md-6">\r\n      Something will go here. Possibly a pie chart. Maybe something cool.\r\n      Lorem ipsum dolor sit amet, etiam suscipit molestie, accumsan aliquam est urna, mi metus vel. Mollis ut in congue eros, ornare ac sagittis donec, quis vel cupiditate elit facilisis, lectus purus eu magnis penatibus, at gravida eu. Enim pellentesque integer lorem, morbi quam, massa nulla, nulla enim. Duis quam facilisis congue, blanditiis metus. Duis scelerisque pellentesque ut nullam nunc, aliquam at in quis quisque ipsum.\r\nPellentesque orci eget. Cras tempus at luctus donec sed, odio volutpat elit ultricies adipisci aenean ligula, arcu ac nunc, suspendisse in, lorem gravida cum. Libero quis. Dui vel potenti, vel vestibulum. Suspendisse cras, sapien eu, id mi arcu ridiculus nibh vitae est, nonummy pulvinar et purus, dignissim risus. Velit non mauris pellentesque, integer mattis.\r\n    </div>\r\n  </div>\r\n  <div class="col-md-3">\r\n    <div class="text-right">\r\n      <h3>Credit vs Debit</h3>\r\n      <select id="l_list" onChange="updateLine()">\r\n          <option value="2015">2015</option>\r\n          <option value="2014">2014</option>\r\n      </select>\r\n    </div>\r\n  </div>\r\n  <div>\r\n    <div class="col-md-12">\r\n      <div class="line_chart">\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n    <script>\r\n      //#load in data, call loadGraph\r\n        var data = ')
        __M_writer(str(types_json))
        __M_writer('\r\n        loadGraph(data);\r\n      //#updateData//\r\n        function updateData() {\r\n          var remove = d3.select(".this_svg").remove()\r\n            //removes current table for filtered\r\n\r\n          var data = ')
        __M_writer(str(types_json))
        __M_writer('\r\n          var x = document.getElementById("d_list").selectedIndex;       \r\n\r\n          if (x == 1) {\r\n            var key2value = selectWhere(data, "Checking");\r\n          }\r\n          else if (x == 2) {\r\n            var key2value = selectWhere(data, "Credit Card");\r\n          }\r\n          else if (x == 3) {\r\n            var key2value = selectWhere(data, "Investments");\r\n          }\r\n          else if (x == 4) {\r\n            var key2value = selectWhere(data, "Savings");\r\n          }\r\n          else if (x == 5) {\r\n            var key2value = selectWhere(data, "Other");\r\n          }\r\n          else{\r\n            loadGraph(data);\r\n          }\r\n        }\r\n\r\n      //#called to create the filtered data\r\n        function selectWhere(data, propertyName) {\r\n          var acc_data = []\r\n          for (var i = 0; i < data.length; i++) {\r\n            if (data[i][2] === propertyName) {\r\n              acc_data[acc_data.length] = data[i];\r\n              //return data[i];\r\n            }\r\n          }\r\n          loadGraph(acc_data);\r\n        }\r\n      //#loads graph\r\n        function loadGraph(data) {\r\n        //#set margins, build svg bar_chart\r\n          var margin = {top: 40, right: 20, bottom: 30, left: 60},\r\n              width = 700 - margin.left - margin.right,\r\n              height = 500 - margin.top - margin.bottom;\r\n\r\n          var x = d3.scale.ordinal()\r\n              .rangeRoundBands([0, width], .2);\r\n\r\n          var y = d3.scale.linear()\r\n              .range([height, 0]);\r\n\r\n          var xAxis = d3.svg.axis()\r\n              .scale(x)\r\n              .orient("bottom");\r\n\r\n          var yAxis = d3.svg.axis()\r\n              .scale(y)\r\n              .orient("left");\r\n\r\n          var tip = d3.tip()\r\n            .attr(\'class\', \'d3-tip\')\r\n            .offset([-10, 0])\r\n            .html(function(d) {\r\n              return "<strong>Acount:</strong> <span style=\'color:red\'>" + d[0] + "</span>" +"<br/>" + \r\n              "<strong>Amount:</strong> <span style=\'color:red\'>" + d[1] + "</span>";\r\n            })\r\n\r\n          var svg = d3.select(".bar_chart").append("svg")\r\n              .attr("width", width + margin.left + margin.right)\r\n              .attr("height", height + margin.top + margin.bottom)\r\n              .attr("id", "svg_bar")\r\n              .attr("class", "this_svg")\r\n            .append("g")\r\n              .attr("id", "g_bar")\r\n              .attr("transform", "translate(" + margin.left + "," + margin.top + ")");\r\n          svg.call(tip);\r\n          //starts the chart at 0, handles if there is only one account\r\n          data[data.length] = ["", 0, ""]\r\n\r\n          x.domain(data.map(function(d) { return d[0]; }));\r\n          y.domain(d3.extent(data, function(d) { return +d[1]; })).nice();\r\n\r\n          /*  ////adds x axis////\r\n            svg.append("g")\r\n                .attr("class", "x axis")\r\n                .attr("id", "g_bar")\r\n                .attr("transform", "translate(0," + height + ")")\r\n                .call(xAxis);\r\n          */\r\n          /* ///Automatic Transition///\r\n            svg.selectAll("g").remove();\r\n            svg.selectAll("text").remove();\r\n          */\r\n          svg.append("g")\r\n              .attr("class", "y axis")\r\n              .attr("id", "g_bar")\r\n              .call(yAxis)\r\n            .append("text")\r\n              .attr("transform", "rotate(-90)")\r\n              .attr("y", 6)\r\n              .attr("dy", ".71em")\r\n              .style("text-anchor", "end");\r\n\r\n            svg.selectAll(".bar")\r\n                .data(data)\r\n            .enter().append("rect")\r\n                .attr("class", function(d) { return d[1] < 0 ? "bar negative" : "bar positive"; })\r\n                .attr("y", function(d) { return y(Math.max(0, d[1])); })\r\n                .attr("x", function(d) { return x(d[0]); })\r\n                .on(\'mouseover\', tip.show)\r\n                .on(\'mouseout\', tip.hide)\r\n                .transition()\r\n                  .ease("elastic")\r\n                .delay(function (d, i) { return i*100; })\r\n                .attr("height", function(d) { return Math.abs(y(d[1]) - y(0)); })\r\n                .attr("width", x.rangeBand())\r\n        /* ///Automatic Transition///\r\n          var rect = svg.selectAll("rect")\r\n            .data(data);\r\n\r\n          rect.attr("id", "update");\r\n\r\n          rect.enter().append("rect")\r\n            .attr("id", "enter")\r\n            .attr("class", function(d) { return d[1] < 0 ? "bar negative" : "bar positive"; })\r\n            .attr("y", function(d) { return y(Math.max(0, d[1])); })\r\n            .attr("x", function(d) { return x(d[0]); })\r\n            .on(\'mouseover\', tip.show)\r\n            .on(\'mouseout\', tip.hide)\r\n            .transition()\r\n              .ease("elastic")\r\n            .delay(function (d, i) { return i*100; })\r\n            .attr("height", function(d) { return Math.abs(y(d[1]) - y(0)); })\r\n            .attr("width", x.rangeBand());\r\n          rect.text(function(d) { return d; });\r\n          rect.exit().remove();\r\n        */\r\n            function type(d) {\r\n              d[1] = +d[1];\r\n              return d;\r\n            }\r\n        }\r\n    </script>\r\n\r\n    <style>\r\n        path.line {\r\n          fill: none;\r\n          stroke: #666;\r\n          stroke-width: 1.5px;\r\n        }\r\n\r\n        path.area {\r\n          fill: #e7e7e7;\r\n        }\r\n\r\n        .axis {\r\n          shape-rendering: crispEdges;\r\n        }\r\n\r\n        .x.axis line {\r\n          stroke: #fff;\r\n        }\r\n\r\n        .x.axis .minor {\r\n          stroke-opacity: .5;\r\n        }\r\n\r\n        .x.axis path {\r\n          display: none;\r\n        }\r\n\r\n        .y.axis line, .y.axis path {\r\n          fill: none;\r\n          stroke: #000;\r\n        }\r\n        .guideline {\r\n          margin-right: 100px;\r\n          float: right;\r\n        }\r\n    </style>\r\n\r\n    <script>\r\n        //load the initial graph data (year 2015)\r\n        var d_data = ')
        __M_writer(str(dc_json))
        __M_writer('\r\n        var data = d_data.filter(function(d) {\r\n            return d[3] == "2015";\r\n          });\r\n        loadLine(data);\r\n\r\n        function parse(date) {\r\n          //parse the dates into month format\r\n            var p = d3.time.format("%Y-%m-%d").parse;\r\n            var o = d3.time.format("%m")\r\n            \r\n            var p_date = p(date)\r\n            var o_date = o(p_date)\r\n            return o_date\r\n          };\r\n\r\n        //preps the filter data\r\n        function updateLine() {\r\n            var remove = d3.select(".svg_line").remove()\r\n              //removes current table for filtered\r\n              \r\n            var data = ')
        __M_writer(str(dc_json))
        __M_writer('\r\n            var x = document.getElementById("l_list").selectedIndex;       \r\n\r\n            if (x == 1) {\r\n              var key2value = selectWhere(data, "2014");\r\n            }\r\n            else{\r\n              var key2value = selectWhere(data, "2015")\r\n            }\r\n          };\r\n\r\n          //#called to create the filtered data\r\n        function selectWhere(data, propertyName) {\r\n            var new_data = data.filter(function(d) {\r\n                return d[3] == propertyName;\r\n              });\r\n            loadLine(new_data);\r\n          };\r\n\r\n        //initial graph load.\r\n        function loadLine(data){\r\n          var margin = {top: 50, right: 60, bottom: 50, left: 60},\r\n              width = 1100 - margin.left - margin.right,\r\n              height = 600 - margin.top - margin.bottom;   \r\n\r\n          // Scales and axes. Note the inverted domain for the y-scale: bigger is up!\r\n          var x = d3.time.scale().range([0, width]),\r\n              y = d3.scale.linear().range([height, 0]),\r\n              xAxis = d3.svg.axis().scale(x).tickSize(-height).tickSubdivide(true),\r\n              yAxis = d3.svg.axis().scale(y).ticks(4).orient("right");\r\n\r\n          // An area generator, for the light fill.\r\n          var area = d3.svg.area()\r\n              .interpolate("monotone")\r\n              .x(function(d) { return x(parse(d[0])); })\r\n              .y0(height)\r\n              .y1(function(d) { return y(+d[1]); });\r\n\r\n          // A line generator, for the dark stroke.\r\n          var line = d3.svg.line()\r\n              .interpolate("monotone")\r\n              .x(function(d) { return x(parse(d[0])); })\r\n              .y(function(d) { return y(+d[1]); });\r\n\r\n\r\n            // Filter to one type\r\n            var credit = data.filter(function(d) {\r\n              return d[2] == "credit";\r\n            });\r\n\r\n            var debit = data.filter(function(d) {\r\n              return d[2] == "debit";\r\n            });\r\n\r\n            // Compute the minimum and maximum date, and the maximum price.\r\n            x.domain([d3.min(debit, function(d) { return parse(d[0]); }), d3.max(debit, function(d) { return parse(d[0]); })]).nice();\r\n            y.domain([d3.min(debit, function(d) { return +d[1]; }), d3.max(credit, function(d) { return +d[1]; })]).nice();\r\n\r\n            // Add an SVG element with the desired dimensions and margin.\r\n            var svg = d3.select(".line_chart").append("svg")\r\n                .attr("width", width + margin.left + margin.right)\r\n                .attr("height", height + margin.top + margin.bottom)\r\n                .attr("class", "svg_line")\r\n              .append("g")\r\n                .attr("transform", "translate(" + margin.left + "," + margin.top + ")")\r\n                \r\n\r\n            // Add the clip path.\r\n            svg.append("clipPath")\r\n                .attr("id", "clip")\r\n              .append("rect")\r\n                .attr("width", width)\r\n                .attr("height", height);\r\n\r\n            // Add the x-axis.\r\n            svg.append("g")\r\n                .attr("class", "x axis")\r\n                .attr("transform", "translate(0," + height + ")")\r\n                .call(xAxis);\r\n\r\n            // Add the y-axis.\r\n            svg.append("g")\r\n                .attr("class", "y axis")\r\n                .attr("transform", "translate(" + width + ",0)")\r\n                .call(yAxis);\r\n\r\n            var colors = d3.scale.category10();\r\n            svg.selectAll(\'.line\')\r\n              .data([credit, debit])\r\n              .enter()\r\n                .append(\'path\')\r\n                  .attr(\'class\', \'line\')\r\n                  .style(\'stroke\', function(d) {\r\n                    return colors(Math.random() * 50);\r\n                  })\r\n                  .attr(\'clip-path\', \'url(#clip)\')\r\n                  .attr(\'d\', function(d) {\r\n                    return line(d);\r\n                  })\r\n\r\n            /* Add \'curtain\' rectangle to hide entire graph */\r\n            var curtain = svg.append(\'rect\')\r\n              .attr(\'x\', -1 * width)\r\n              .attr(\'y\', -1 * height)\r\n              .attr(\'height\', height)\r\n              .attr(\'width\', width)\r\n              .attr(\'class\', \'curtain\')\r\n              .attr(\'transform\', \'rotate(180)\')\r\n              .style(\'fill\', \'#ffffff\')\r\n\r\n            /* Optionally add a guideline */\r\n            var guideline = svg.append(\'line\')\r\n              .attr(\'stroke\', \'#333\')\r\n              .attr(\'stroke-width\', 0)\r\n              .attr(\'class\', \'guide\')\r\n              .attr(\'x1\', 1)\r\n              .attr(\'y1\', 1)\r\n              .attr(\'x2\', 1)\r\n              .attr(\'y2\', height)\r\n\r\n            /* Create a shared transition for anything we are animating */\r\n            var t = svg.transition()\r\n              .delay(750)\r\n              .duration(6000)\r\n              .ease(\'linear\')\r\n              .each(\'end\', function() {\r\n                d3.select(\'line.guide\')\r\n                  .transition()\r\n                  .style(\'opacity\', 0)\r\n                  .remove()\r\n              });\r\n\r\n            t.select(\'rect.curtain\')\r\n              .attr(\'width\', 0);\r\n            t.select(\'line.guide\')\r\n              .attr(\'transform\', \'translate(\' + width + \', 0)\')\r\n\r\n            d3.select("#show_guideline").on("change", function(e) {\r\n              guideline.attr(\'stroke-width\', this.checked ? 1 : 0);\r\n              curtain.attr("opacity", this.checked ? 0.75 : 1);\r\n            })\r\n\r\n          // Parse dates and numbers. We assume values are sorted by date.\r\n          function type(d) {\r\n            d[0] = parse(d[0]);\r\n            d[1] = +d[1];\r\n            console.log("here")\r\n            return d;\r\n          } \r\n        };\r\n    </script> \r\n    </body>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"27": 0, "36": 1, "69": 63, "41": 418, "47": 3, "55": 3, "56": 58, "57": 58, "58": 65, "59": 65, "60": 244, "61": 244, "62": 265, "63": 265}, "filename": "C:\\Python34\\Lib\\site-packages\\django\\bin\\finance\\dashboard\\templates/dashboard.html", "uri": "dashboard.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
