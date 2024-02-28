$(document).ready(function() {
  $("#add_item_button").on("click", function() {
    // Create a new <li> element
    var newItem = $("<li>").text("Item");
    
    // Append the new <li> element to the existing UL with class "my_list"
    $("ul.my_list").append(newItem);
  });
});
