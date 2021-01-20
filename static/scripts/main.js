
$(document).ready(function(){

    $('.sidenav').sidenav();

    $("select").formSelect();

     $('textarea#bike_description').characterCounter();
     /* Year Picker documentation on https://www.codehim.com/date-time/jquery-datepicker-year-only/ */
     $(".yearpicker").yearpicker({
      startYear: 1900,
      endYear: 2021,
   });

    /*MediumZoom Javascript https://github.com/francoischalifour/medium-zoom */
    mediumZoom(document.querySelectorAll('[data-zoomable]'),{
        background: "rgba(255,255,255,.8)"
    });

    /* Scroll to top button code from @rdallaire on CodePen https://codepen.io/rdallaire/pen/apoyx */
$(window).scroll(function () {
    if ($(this).scrollTop() >= 600) {
        // If page is scrolled more than 600px
        $("#return-to-top").fadeIn(100); // Fade in the arrow
    } else {
        $("#return-to-top").fadeOut(100); // Else fade out the arrow
    }
});
$("#return-to-top").click(function () {
    // When arrow is clicked
    $("body,html").animate(
        {
            scrollTop: 0, // Scroll to top of body
        },
        500
    );
});

})