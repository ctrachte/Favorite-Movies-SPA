class Movie():
	"""This class provides a way to store movie related information.
	Attributes:
	-title is the movie's title
	-storyline is a brief plot synopsis
	-poster_image_url is the poster art for the movie
	-trailer_youtube_url is the trailer for the movie taken from youtube, 
		*also might be a movie clip if the trailer is copyrwite protected*
	-rating is the motion picture association of America's rating for the movie
	-director is the movie's director
	-genre is the movie's genre
	-duration is the how long the movie is in h/m format

	"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating, director, genre, year, duration):
		"""initializes Movie class with all respective variables"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.rating = rating
		self.director = director
		self.genre = genre
		self.year = year
		self.duration = duration