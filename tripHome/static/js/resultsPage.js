$(document).ready(function () {
  // ajax call with search data
  var token = "{{csrf_token}}";
  $.ajax({
    headers: { "X-CSRFToken": token },
    method: "POST",
    url: "results",
    data: { requestData: localStorage.getItem("searchItems") },
    beforeSend: function () {
      $(".loader").show();
    },
    success: function (data) {
      showData(data);
    },
    error: function (data) {
      alert("it didnt work");
    },
    complete: function (data) {
      $(".loader").hide();
    },
  });
});

function showData(data) {
  parsed_data = JSON.parse(data);
  document.getElementById("data").innerHTML = data;
}
