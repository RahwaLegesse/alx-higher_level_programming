$(document).ready(function() {
        // Select the <div> with ID "toggle_header"
        $("#toggle_header").click(function() {
            const headerElement = $("header");

            if (headerElement.hasClass("red")) {
                headerElement.removeClass("red").addClass("green");
            } else {
                headerElement.removeClass("green").addClass("red");
            }
        });
    });
