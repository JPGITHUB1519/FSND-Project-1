$('.carousel').slick({
	// infinite: false,
	// centerPadding: '120px',
	// centerMode: true,
	slidesToShow: 8,
	swipeToSlide: true,
	responsive: [
	{
	  breakpoint: 1795,
	  settings: {
	    slidesToShow: 7,
	    slidesToScroll: 7,
	    infinite: true,
	    dots: true
	  }
	},	
	{
	  breakpoint: 1500,
	  settings: {
	    slidesToShow: 6,
	    slidesToScroll: 6,
	    infinite: true,
	    dots: true
	  }
	},	
	{
	  breakpoint: 1300,
	  settings: {
	    slidesToShow: 5,
	    slidesToScroll: 5,
	    infinite: true,
	    dots: true
	  }
	},
	{
	  breakpoint: 1150,
	  settings: {
	    slidesToShow: 4,
	    slidesToScroll: 4,
	    infinite: true,
	    dots: true
	  }
	},
	{
	  breakpoint: 900,
	  settings: {
	    slidesToShow: 3,
	    slidesToScroll: 3,
	    infinite: true,
	    dots: true
	  }
	},	
	{
	  breakpoint: 700,
	  settings: {
	    slidesToShow: 2,
	    slidesToScroll: 2
	  }
	},
	{
	  breakpoint: 480,
	  settings: {
	    slidesToShow: 1,
	    slidesToScroll: 1
	  }
	}
	]	
})
// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
});
// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.movie-tile', function (event) {
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
      'id': 'trailer-video',
      'type': 'text-html',
      'src': sourceUrl,
      'frameborder': 0
    }));
});

var storylineHeader = $('.storylineHeader')
var storylineP = $('.storyline')

$('.movie-tile').mouseenter(function(){
	storylineHeader.html('Plot Summary:');
	storylineP.html($(this).attr('storyline'));
}).mouseleave(function(){
	storylineHeader.html("");
	storylineP.html("");
});