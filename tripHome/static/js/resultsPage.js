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
  obj = JSON.parse(data);
  if (obj.Raleigh != null) {
    ral_list = Object.entries(obj.Raleigh);
    text = "<h3>Raleigh</h3><ul>";
    for (i = 0; i < ral_list.length; i++) {
      text += "<li>" + ral_list[i] + "</li>";
    }
    text += "</ul>";
    document.getElementById("ral").innerHTML = text;
  }
  if (obj.Charlotte != null) {
    char_list = Object.entries(obj.Charlotte);
    text = "<h3>Charlotte</h3><ul>";
    for (i = 0; i < char_list.length; i++) {
      text += "<li>" + char_list[i] + "</li>";
    }
    text += "</ul>";
    document.getElementById("char").innerHTML = text;
  }
  if (obj.Asheville != null) {
    ashe_list = Object.entries(obj.Asheville);
    text = "<h3>Asheville</h3><ul>";
    for (i = 0; i < ashe_list.length; i++) {
      text += "<li>" + ashe_list[i] + "</li>";
    }
    text += "</ul>";
    document.getElementById("char").innerHTML = text;
  }
}
