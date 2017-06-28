 $(document).ready(function() {

   // Get data
     var url = $('#url').val();
     var shortId = $('#shortid').val();
     var csrfToken = $("input[name=csrfmiddlewaretoken]").val();

  // Ready data
     var data = {
       'url' : url,
       'shortid': shortId,
       'csrfmiddlewaretoken' : csrfToken
     };


     $('#submitButton').click(function() {
       $.ajax({
         type: "POST",
         url: "makeshort/",
         data: data,
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
