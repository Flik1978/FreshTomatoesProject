import webbrowser


class Movie():

    """This class takes in the movie title, poster image link and youtube link,
    creates a movie object and returns to entertainment_center."""

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Creates a movie object with the"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
