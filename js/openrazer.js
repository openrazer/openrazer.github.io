/*
 * Designed by @lah7 for the OpenRazer project.
 *
 * Copyright (C) 2016-2020 Luke Horwell (lah7)
 * Licensed under CC BY-SA 4.0
 */

$(document).ready(function() {
  // Floating "Mini" Navigation Bar
  $(document).scroll(function() {
    if ( $(this).scrollTop() > 128 ) {
        $('#nav-menu').addClass('nav-sticky');
        $('#nav-menu').removeClass('nav-top');
        $('#mini-logo-text').fadeIn();
    } else {
        $('#nav-menu').removeClass('nav-sticky');
        $('#nav-menu').addClass('nav-top');
        $('#mini-logo-text').fadeOut();
    }
  });
  $(document).scroll();

  // Add an 'active' class when download panels are opened.
  $('.panel-collapse').on('show.bs.collapse', function() {
    $(this).parent().addClass('active');
  });

  $('.panel-collapse').on('hide.bs.collapse', function() {
    $(this).parent().removeClass('active');
  });
});

// Auto-open OS installation instructions if specified with hash.
if (window.location.hash) {
    const hash = window.location.hash.substring(1);
    $('#' + hash).collapse('show');
    $('#' + hash).parent().addClass("active");
    $('#' + hash).focus();
    $(window).scrollTop($("#" + hash).offset().top - 128);
}
