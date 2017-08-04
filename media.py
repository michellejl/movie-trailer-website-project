import webbrowser


class Movie():
    """ This class provides a way to store information related to movies. """

    def __init__(self, title, storyline, year, poster_image, trailer):
        self.title = title
        self.storyline = storyline
        self.release_year = year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
