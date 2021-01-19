
$(document).ready(function(){

    $('.sidenav').sidenav();

    $("select").formSelect();

     $('textarea#bike_description').characterCounter();

    /*MediumZoom Javascript https://github.com/francoischalifour/medium-zoom */
    mediumZoom(document.querySelectorAll('[data-zoomable]'),{
        background: "rgba(255,255,255,.8)"
    });

})