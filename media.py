'''this file stores the classes used in the creation of the final website
The Show class is currently unused but is for the future addition of TV shows'''

import webbrowser

class Video():
	"""Base Video class that movies and tv shows can inherit"""
	def __init__(self, title, storyline):
		self.title = title
		self.storyline = storyline

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

class Movie(Video):
	"""This class provides a way to store movie related information"""

	def __init__(self, title, storyline, year, poster_image,
				 trailer_youtube):
		Video.__init__(self, title, storyline)
		self.year = year
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

class Show(Video):
	"""This class provides a way to store TV Show related information"""

	def __init__(self, title, storyline, episodes, poster_image,
				 trailer_youtube):
		Video.__init__(self, title, storyline)
		self.episodes = episodes
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
