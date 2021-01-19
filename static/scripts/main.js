
$(document).ready(function(){

    $('.sidenav').sidenav();
    $(".collapsible").collapsible();
    $("select").formSelect();

    /*MediumZoom Javascript https://github.com/francoischalifour/medium-zoom */
    mediumZoom(document.querySelectorAll('[data-zoomable]'),{
        background: "rgba(255,255,255,.6)"
    });

    $('textarea#bike_description').characterCounter();

})