$(document).ready(function(){

	
    var data_dict = localStorage.getItem("searchItems")

    var token = '{{csrf_token}}';
    $.ajax({
        headers: { "X-CSRFToken": token },
        method: 'POST',
        url: 'ajax/submit/',
        data: {'requestData': JSON.stringify(data_dict)},
        success: function (data) {
            
        },
        error: function (data) {
             alert("it didnt work");
        }
    });

        

});	



    
