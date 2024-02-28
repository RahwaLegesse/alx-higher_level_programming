$(document).ready(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    method: "GET",
    success: function(data) {
      var movies = data.results;
      var movieList = $("#list_movies");

      // Iterate through each movie and create a list item
      $.each(movies, function(index, movie) {
        var listItem = $("<li>").text(movie.title);
        movieList.append(listItem);
      });
    },
    error: function() {
      // Handle any errors (e.g., network issues, invalid URL)
      console.error("Error fetching movie data.");
    }
  });
});
