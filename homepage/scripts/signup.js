$(function () {
  
  $('#signup').ajaxForm(function() { 
    }); 

  $('#id_username').on('change', function() {
    var username = $('#id_username').val();
    console.log(username);

    $.ajax({
      url: '/homepage/signup.check_username/',
      
      data: {
        u: username,
      },//data
      
      type: "POST",
      
      success: function(resp) {
        $('#id_username_message').remove()
        if (resp == 1) {
          $('#id_username_message').remove()
          $('#id_username').after('<span id="id_username_message">Available!</span>')
        }else{
          $('#id_username_message').remove()
          $('#id_username').after('<span id="id_username_message">Unavailable!</span>')
        }//if

      },//success

    });//ajax

  });//change

});//ready