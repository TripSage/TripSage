$(document).ready(function(){


    var token = '{{csrf_token}}';
    $.ajax({
        headers: { "X-CSRFToken": token },
        method: 'POST',
        url: 'results',
        data: {'requestData': localStorage.getItem("searchItems")},
        success: function (data) {
            console.log("Hi");
        },
        error: function (data) {
             alert("it didnt work");
        }
    });

        

});	



    
