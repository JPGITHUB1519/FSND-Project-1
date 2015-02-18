'''this file holds the constructor for the media center that will
build the final webpage from the template based on a list of movie objects'''

import webbrowser
import os
import re
import page_skeleton


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += pageSkeleton.movie_tile_content.format(
            movie_title=movie.title+"("+movie.year+")",
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_storyline=movie.storyline
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  movie_content = create_movie_tiles_content(movies)
  final_rendered_content = pageSkeleton.html.format(movieplaceholder=movie_content)
  # Output the file
  print final_rendered_content
  output_file.write(final_rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible