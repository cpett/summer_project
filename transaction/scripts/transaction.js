$(function () {
  console.log('loaded js');

  $('#instructions_dialog').modal({
    show: false,
  });//modal

  $('#show_instructions_dialog').on('click', function() {
    console.log('here');
    $('#instructions_dialog').modal('show');

 //  var body = d3.select("body");
	// body.style("color", "black");
	// body.style("background-color", "blue");
	////////////////////d3 test//////////////
	// d3.select("body")
 //    .style("color", "black")
 //    .style("background-color", "black");

	});//showmodal
});//ready

(function(document) {
	'use strict';

	var LightTableFilter = (function(Arr) {

		var _input;

		function _onInputEvent(e) {
			_input = e.target;
			console.log('onInput')
			var tables = document.getElementsByClassName(_input.getAttribute('data-table'));
			Arr.forEach.call(tables, function(table) {
				Arr.forEach.call(table.tBodies, function(tbody) {
					Arr.forEach.call(tbody.rows, _filter);
				});
			});
		}

		function _filter(row) {
			var text = row.textContent.toLowerCase(), val = _input.value.toLowerCase();
			row.style.display = text.indexOf(val) === -1 ? 'none' : 'table-row';
		}

		return {
			init: function() {
				var inputs = document.getElementsByClassName('light-table-filter');
				Arr.forEach.call(inputs, function(input) {
					input.oninput = _onInputEvent;
				});
			}
		};
	})(Array.prototype);

	document.addEventListener('readystatechange', function() {
		if (document.readyState === 'complete') {
			LightTableFilter.init();
		}
	});

})(document);
