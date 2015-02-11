'''this file contains a list of movie objects and it calls fresh_tomatoes
as a constructor to build the final website based on this list'''

import fresh_tomatoes
from media import *

# all of our movie objects built from the Movie class in media.py
toy_story = Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"1995",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = Movie("Avatar",
					 "A marine on an alien planet",
					 "2009",
					 "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

shawshank_redemption = Movie("Shawshank Redemption",
					 "A man spends time in jail after being accused of murder",
					 "1994",			 
					 "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
					 "www.youtube.com/watch?v=6hB3S9bIaco")

godfather = Movie("Godfather",
					 "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
					 "1972",			 
					 "http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@.SX220_.jpg",
					 "www.youtube.com/watch?v=sY1S34973zA")

godfather2 = Movie("Godfather II",
				   "The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on his crime syndicate stretching from Lake Tahoe, Nevada to pre-revolution 1958 Cuba.",
				   "1974",				   
				   "http://ia.media-imdb.com/images/M/MV5BNDc2NTM3MzU1Nl5BMl5BanBnXkFtZTcwMTA5Mzg3OA@@.SX220.jpg",
				   "www.youtube.com/watch?v=8PyZCU2vpi8")

foreast_gump = Movie("Forrest Gump",
					 "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
					 "1994",
					 "http://ia.media-imdb.com/images/M/MV5BMTI1Nzk1MzQwMV5BMl5BanBnXkFtZTYwODkxOTA5.SX220.jpg",
					 "www.youtube.com/watch?v=eYSnxZKTZzU")

star_wars = Movie("Star Wars",
				  "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a wookiee and two droids to save the universe from the Empire's world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader.",
				  "1977",
				  "http://ia.media-imdb.com/images/M/MV5BMTU4NTczODkwM15BMl5BanBnXkFtZTcwMzEyMTIyMw@@.SX220.jpg",
				  "www.youtube.com/watch?v=1g3_CFmnU7k")

pulp_fiction = Movie("Pulp Fiction",
	                 "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
	                 "1994",
	                 "http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4.SX220.jpg",
	                 "https://www.youtube.com/watch?v=dZWPL9deY7I")

spirited_away = Movie("Spirited Away",
	                  "In the middle of her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and monsters; where humans are changed into beasts.",
	                  "2001",
	                  "http://ia.media-imdb.com/images/M/MV5BMjYxMDcyMzIzNl5BMl5BanBnXkFtZTYwNDg2MDU3.SX220.jpg",
	                  "https://www.youtube.com/watch?v=ByXuk9QqQkk")
brothers_bloom = Movie("The Brothers Bloom",
					   "The Brothers Bloom are the best con men in the world, swindling millionaires with complex scenarios of lust and intrigue. Now they've decided to take on one last job - showing a beautiful and eccentric heiress the time of her life with a romantic adventure that takes them around the world.",
					   "2008",
					   "http://ia.media-imdb.com/images/M/MV5BMTM3NTY3MDI2NF5BMl5BanBnXkFtZTcwNjUwNTU4MQ@@.SX220.jpg",
					   "https://www.youtube.com/watch?v=qYMsvFUdPEY")

# list of movie objects that will be used when creating the html page
movies = [toy_story, avatar, shawshank_redemption, godfather, godfather2, foreast_gump, star_wars, pulp_fiction, spirited_away, brothers_bloom]

# call the actual constructor and open the webpage in a browser
fresh_tomatoes.open_movies_page(movies)
