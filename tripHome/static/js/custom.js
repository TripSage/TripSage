$(document).ready(function () {
  "use strict";

  $(window).on("scroll", function () {
    if ($(this).scrollTop() > 600) {
      $(".return-to-top").fadeIn();
    } else {
      $(".return-to-top").fadeOut();
    }
  });

  $(".return-to-top").on("click", function () {
    $("html, body").animate(
      {
        scrollTop: 0,
      },
      1500
    );

    return false;
  });

  $("#slider-range").slider({
    range: true,
    min: 0,
    max: 12000,
    values: [2677, 9241],
    slide: function (event, ui) {
      $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
    },
  });
  $("#amount").val(
    "$" +
      $("#slider-range").slider("values", 0) +
      " - $" +
      $("#slider-range").slider("values", 1)
  );

  // 5. datepicker
  $('[data-toggle="datepicker"]').datepicker();

  // 6. Smooth Scroll spy

  $(".header-area").sticky({
    topSpacing: 0,
  });

  //=============

  $("li.smooth-menu a").bind("click", function (event) {
    event.preventDefault();
    var anchor = $(this);
    $("html, body")
      .stop()
      .animate(
        {
          scrollTop: $(anchor.attr("href")).offset().top - -1,
        },
        1200,
        "easeInOutExpo"
      );
  });

  $("body").scrollspy({
    target: ".navbar-collapse",
    offset: 0,
  });

  // 7.animation support

  $(window).load(function () {
    $(".about-us-txt h2")
      .removeClass("animated fadeInUp")
      .css({ opacity: "0" });
    $(".about-us-txt button")
      .removeClass("animated fadeInDown")
      .css({ opacity: "0" });
  });

  $(window).load(function () {
    $(".about-us-txt h2").addClass("animated fadeInUp").css({ opacity: "0" });
    $(".about-us-txt button")
      .addClass("animated fadeInDown")
      .css({ opacity: "0" });
  });
});

// Initializing the forms as select2, select2 provides a flexibility over select tag
$("#destinationSelection").select2({
  maximumSelectionLength: 2,
});

$("#sourceSelection").select2({
  maximumSelectionLength: 1,
});

$("#travelSelection").select2({
  maximumSelectionLength: 2,
});

$("#transportSelection").select2({
  maximumSelectionLength: 2,
});

// Function which collects the user data in localstorage
function saveData() {
  destination_choices = [];
  var destinationChoice = $("#destinationSelection").select2("data");
  destinationChoice.forEach(function (d) {
    destination_choices.push(d.id);
  });
  var destination = destination_choices[0];
  var destination_selected = destination_choices;

  data_dict = {};

  source_choices = [];
  var sourceChoice = $("#sourceSelection").select2("data");
  sourceChoice.forEach(function (d) {
    source_choices.push(d.id);
  });
  source_choices = source_choices[0];

  trip_kinds = [];
  var tripKind = $("#travelSelection").select2("data");
  tripKind.forEach(function (d) {
    trip_kinds.push(d.id);
  });

  mode_transports = [];
  var modeTransport = $("#transportSelection").select2("data");
  modeTransport.forEach(function (d) {
    mode_transports.push(d.id);
  });

  start_date = $("#start_date")[0].value;
  end_date = $("#end_date")[0].value;

  members_count = $("#members_count")[0].value;
  budget_range = $("#amount")[0].value;

  data_dict["source"] = source_choices;
  data_dict["destination"] = destination;
  data_dict["destination_selected"] = destination_selected;
  data_dict["tripType"] = trip_kinds;
  data_dict["modeTransport"] = modeTransport;
  data_dict["startDate"] = start_date;
  data_dict["endDate"] = end_date;

  // clear the local storage
  localStorage.clear();

  //save the data to local storage
  localStorage.setItem("searchItems", JSON.stringify(data_dict));

  //redirect to results page
  var url = "search";
  document.location.href = url;
}
