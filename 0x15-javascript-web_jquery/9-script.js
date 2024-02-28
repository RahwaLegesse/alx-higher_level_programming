$(document).ready(function() {
  // Make an AJAX request to fetch the translation
  $.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    method: "GET",
    success: function(data) {
      // Extract the translated word for "hello"
      var translatedHello = data.hello;

      $("#hello").text(translatedHello);
    },
    error: function() {
      console.error("Error fetching translation data.");
    }
  });
});
