 $(document).ready( function hello() {
     $('#submitButton').click(function() {
     $.ajax({
     type: "POST",
     url: "makeshort/",
     data: {
     'url' : $('#url').val(),
     'shortid': $('#shortid').val(),
     'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
     },
     success: returnSuccess,
     dataType: 'json'
     });
     });
  
    function returnSuccess(data, textStatus, jqXHR) {
     if(data.url) {
     $('#url-result').text(data.url);
     $('#url').val("");
     $('#shortid').val("");
     } else {
     $('#url-result').text("Do not submit blank."); 
     }
    }
});
