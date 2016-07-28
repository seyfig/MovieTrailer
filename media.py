import webbrowser


class Movie:
    """"Movie Class stores movie related information"""
    def __init__(
        self,
        movie_id,
        movie_title,
        movie_storyline,
        movie_poster_image_url,
        movie_pictures,
        movie_trailer_url,
        movie_release_date,
        movie_actors
    ):
        self.movie_id = movie_id
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.picture = movie_pictures
        self.trailer_youtube_url = movie_trailer_url
        self.release_date = movie_release_date
        self.actors = movie_actors
        self.user_comments = []
    # show_trailer function opens the trailer_url in webbrowser

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    # add_comment function adds user comment to the movie

    def add_comment(self, user_comment):
        self.user_comments.append(user_comment)
