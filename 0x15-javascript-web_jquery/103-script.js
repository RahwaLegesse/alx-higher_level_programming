<DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="103-script.js"></script>
    <script>
        // Event listener for button click or ENTER key press
$(document).ready(function() {
  $("#btn_translate").on("click", function() {
    fetchTranslation();
  });

  $("#language_code").on("keypress", function(event) {
    if (event.key === "Enter") {
      fetchTranslation();
    }
  });
});

// Fetch the translation from the API
function fetchTranslation() {
  const languageCode = $("#language_code").val(); // Get the language code from the input field

  $.get(`https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`, function(data) {
    const translation = data.hello; // Extract the translation from the API response
    $("#hello").text(translation); // Display the translation in the DIV#hello element
  });
}

    </script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
