$(document).ready(function () {
  
  // ajax call with search data
  var token = "{{csrf_token}}";
  $.ajax({
    headers: { "X-CSRFToken": token },
    method: "POST",
    url: "results",
    data: { requestData: localStorage.getItem("searchItems") },
    success: function (data) {
      document.getElementById("data").innerHTML = data;
    },
    error: function (data) {
      alert("it didnt work");
    },
  });
});
