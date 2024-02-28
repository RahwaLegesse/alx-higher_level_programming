<DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="101-script.js"></script>
    <script>
        // Add a new <li> element to the list
function addItem() {
  const newItem = $("<li>").text("Item");
  $("ul.my_list").append(newItem);
}

// Remove the last <li> element from the list
function removeItem() {
  $("ul.my_list li:last-child").remove();
}

// Clear all elements from the list
function clearList() {
  $("ul.my_list").empty();
}

// Event listeners for button clicks
$(document).ready(function() {
  $("#add_item").on("click", addItem);
  $("#remove_item").on("click", removeItem);
  $("#clear_list").on("click", clearList);
});

    </script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
  </body>

