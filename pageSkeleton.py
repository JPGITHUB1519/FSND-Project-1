'''This file is a template used to create the final web page'''

# the primary structure or skeleton of the website, minus the movie containers
html = '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
	<link rel="stylesheet" href="support/slick.css">
	<link rel="stylesheet" href="support/slick-theme.css">
	<link rel="stylesheet" href="support/style.css">
	<script src="support/jquery-2.1.3.min.js"></script>
	<script src="support/slick.min.js"></script>
  <link rel="stylesheet" href="support/bootstrap.min.css">
  <script src="support/bootstrap.min.js"></script>
</head>

<body>

    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Click/Touch and drag to scroll posters.  Click a poster to view the trailer.</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid">
    	<div class="row">
		    <div class="carousel col-md-12">
          {movieplaceholder}
        </div>
      </div> 
      <div class="row">
        <div class="text-center col-md-12">
          <h3 class="storylineHeader"></h3>
          <p class="storyline"></p>
        </div>
      </div>
    </div>

<script src="support/main.js"></script>

</body>
</html>

'''

# A single movie entry html template that will be repeated for each Movie
movie_tile_content = '''
<div class="movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" storyline="{movie_storyline}">
  <img src="{poster_image_url}" width="220" height="342">
  <h4>{movie_title}</h4>
</div>  
'''