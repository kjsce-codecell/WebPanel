function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



 function SaveData(form_id){
	var pre_id = "present"+form_id;
	var paid_id = "paid"+form_id;
	paid = (document.getElementById(paid_id).checked ? 1 : 0);
	present = (document.getElementById(pre_id).checked ? 1 : 0);
	// console.log("paid: " + paid);
	// console.log("present: " + present);
	var csrftoken = getCookie('csrftoken');
	data = {
		"id": form_id,
		"paid": paid,
		"present": present 
	};
	makeCall(data,csrftoken);
  	

};


function makeCall(data,csrftoken){
	$.ajaxSetup({
    beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
	});
	
	$.post({
  		type: "POST",
  		url: "http://localhost:8000/register/save/",
  		data: data,
  	
  	}).done(function(data){ showMessage(data) });
}

function showMessage(message){
	
	var message_box = document.getElementById('message');
	console.log(message_box);
	message_box.innerHTML = message;
	$("#message").show().delay(2000).fadeOut();
}