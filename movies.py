import webbrowser
import fresh_tomatoes
class Movie:
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube 
        


conjuring2=Movie("conjuring2","it's a horror movie","https://upload.wikimedia.org/wikipedia/en/b/b9/Conjuring_2.jpg","https://www.youtube.com/watch?v=VFsmuRPClr4")
avengers=Movie("avengers","A movie based on marvel comics","https://en.wikipedia.org/wiki/The_Avengers_(2012_film)#/media/File:TheAvengers2012Poster.jpg","https://www.youtube.com/watch?v=eOrNdBpGMv8")
movies=[conjuring2,avengers] #We can further add as many movies as we can
fresh_tomatoes.open_movies_page(movies)
