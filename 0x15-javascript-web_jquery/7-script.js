$(document).ready(function() {
  // Make an AJAX request to fetch the character data
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    method: "GET",
    success: function(data) {
      // Extract the character name from the response
      var characterName = data.name;

      // Update the text content of the DIV#character
      $("#character").text(characterName);
    },
    error: function() {
      // Handle any errors (e.g., network issues, invalid URL)
      console.error("Error fetching character data.");
    }
  });
});
