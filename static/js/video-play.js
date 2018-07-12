$(document).ready(function(){

$('#play-video,#play-video2,#play-video3,#play-video4').on('click', function(e) {
        e.preventDefault();
        $('#video-overlay').addClass('open');
        $("#video-overlay").append('<iframe width="560" height="315" src="https://www.youtube.com/embed/kSoO2KjVVG4" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>');
    });

    $('.video-overlay, .video-overlay-close').on('click', function(e) {
        e.preventDefault();
        close_video();
    });

    $(document).keyup(function(e) {
        if (e.keyCode === 27) { close_video(); }
    });

    function close_video() {
        $('.video-overlay.open').removeClass('open').find('iframe').remove();
    };






});