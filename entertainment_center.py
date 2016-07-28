import fresh_tomatoes
import media

# assign array of movies in order to keep track of movies data
movies = []
# Add data of The Shawshank Redemption

movies.append(
    media.Movie(
        "the_shawshank_redemption",
        "The Shawshank Redemption",
        "Two imprisoned men bond over a number of years, finding solace and "
        "eventual redemption through acts of common decency.",
        "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTg"
        "wMDU2MjEyMDE@._V1_SX640_SY720_.jpg",
        ["http://ia.media-imdb.com/images/M/MV5BMTQ1ODM2MjY3OV5BMl5BanBnXkFtZT"
            "gwMTU2MjEyMDE@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMTM0NjUxMDk5MF5BMl5BanBnXkFtZT"
            "cwNDMxNDY3Mw@@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMTkzMTY0MjE5MV5BMl5BanBnXkFtZT"
            "cwODMxNDY3Mw@@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMTgxMTU1MDkwOV5BMl5BanBnXkFtZT"
            "cwMDQxNDY3Mw@@._V1__SX640_SY720_.jpg"
         ],
        "https://www.youtube.com/watch?v=NmzuHjWmXOc",
        "1994-10-14",
        ["Tim Robbins", "Morgan Freeman", "Bob Gunton"]
        ))
# Add data of The Godfather: Part II

movies.append(
    media.Movie(
        "the_godfather_part2",
        "The Godfather: Part II",
        "The early life and career of Vito Corleone in 1920s New York is "
        "portrayed while his son, Michael, expands and tightens his grip "
        "on his crime syndicate stretching from Lake Tahoe, Nevada to "
        "pre-revolution 1958 Cuba.",
        "http://ia.media-imdb.com/images/M/MV5BNDc2NTM3MzU1Nl5BMl5BanBnXkFtZTc"
        "wMTA5Mzg3OA@@._V1_SX640_SY720_.jpg",
        ["http://ia.media-imdb.com/images/M/MV5BMTg2NTg1Nzg3Ml5BMl5BanBnXkFtZT"
         "cwNzEzMDU4Mg@@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMjMyNTk5NzA4Nl5BMl5BanBnXkFtZT"
         "gwNzc3NjIwMjE@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMTQ3NzcxNzM4N15BMl5BanBnXkFtZT"
         "gwMTg3NjIwMjE@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMTg4MDI2MTU1NV5BMl5BanBnXkFtZT"
         "gwNjE4NjIwMjE@._V1__SX640_SY720_.jpg"
         ],
        "https://www.youtube.com/watch?v=qJr92K_hKl0",
        "1974-12-20",
        ["Al Pacino", "Robert De Niro", "Robert Duvall"]
        ))
# Add data of The Dark Knight

movies.append(
    media.Movie(
        "the_dark_knight",
        "The Dark Knight",
        "When the menace known as the Joker wreaks havoc and chaos on the "
        "people of Gotham, the caped crusader must come to terms with one "
        "of the greatest psychological tests of his ability to fight "
        "injustice.",
        "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTc"
        "wODAyMTk2Mw@@._V1_SX640_SY720_.jpg",
        ["http://ia.media-imdb.com/images/M/MV5BMTkyMjQ4ODk1NF5BMl5BanBnXkFtZT"
         "cwMjcxMTk2Mw@@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMjIyMzI3MTk0Nl5BMl5BanBnXkFtZT"
         "cwODYxMTk2Mw@@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMTQ0NjE5ODQwMV5BMl5BanBnXkFtZT"
         "cwMTcxMTk2Mw@@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMTU5NTE5NjIwM15BMl5BanBnXkFtZT"
         "cwMjAyOTg2MQ@@._V1__SX640_SY720_.jpg"
         ],
        "https://www.youtube.com/watch?v=RPy5qYlTlRY",
        "2008-07-18",
        ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]
        ))
# Add data of Pulp Fiction

movies.append(
    media.Movie(
        "pulp_fiction",
        "Pulp Fiction",
        "The lives of two mob hit men, a boxer, a gangster's wife, and a pair "
        "of diner bandits intertwine in four tales of violence and redemption"
        ".",
        "http://ia.media-imdb.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTg"
        "wNjA5MDc3NjE@._V1_SX640_SY720_.jpg",
        ["http://ia.media-imdb.com/images/M/MV5BMTQ2MDk3ODAwMV5BMl5BanBnXkFtZT"
         "gwNzE4OTEwMjE@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BNTY1MzgzOTYxNV5BMl5BanBnXkFtZT"
         "gwMDI4OTEwMjE@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMTAxMzE0NTE1OTVeQTJeQWpwZ15BbW"
         "U4MDk5OTI4OTEx._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMTAyODE2MzUxNzheQTJeQWpwZ15BbW"
         "U4MDYwMDM4OTEx._V1__SX640_SY720_.jpg"
         ],
        "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
        "1994-10-14",
        ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]
        ))
# Add data of The Lord of the Rings: The Return of the King

movies.append(
    media.Movie(
        "the_Lord_of_the_Rings_the_return_of_the_king",
        "The Lord of the Rings: The Return of the King",
        "Gandalf and Aragorn lead the World of Men against Sauron's army to "
        "draw his gaze from Frodo and Sam as they approach Mount Doom with the"
        " One Ring.",
        "http://ia.media-imdb.com/images/M/MV5BMjE4MjA1NTAyMV5BMl5BanBnXkFtZTc"
        "wNzM1NDQyMQ@@._V1_SX640_SY720_.jpg",
        ["http://ia.media-imdb.com/images/M/MV5BMTM1Nzc5MzA0Ml5BMl5BanBnXkFtZT"
         "cwNjg1MzUyMQ@@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMTk1ODY0NDg2M15BMl5BanBnXkFtZT"
         "cwNTU2MTk2Mw@@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMTMzNzQwODg2OV5BMl5BanBnXkFtZT"
         "cwMzE2MTk2Mw@@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMTgzODk0MTQ0Nl5BMl5BanBnXkFtZT"
         "cwNDE2MTk2Mw@@._V1__SX640_SY720_.jpg"
         ],
        "https://www.youtube.com/watch?v=r5X-hFf6Bwo",
        "2003-12-17",
        ["Elijah Wood", "Viggo Mortensen", "Ian McKellen"]
        ))
# Add data of Fight Club

movies.append(
    media.Movie(
        "fight_club",
        "Fight Club",
        "An insomniac office worker, looking for a way to change his life, "
        "crosses paths with a devil-may-care soap maker, forming an "
        "underground fight club that evolves into something much, much "
        "more...",
        "http://ia.media-imdb.com/images/M/MV5BMjIwNTYzMzE1M15BMl5BanBnXkFtZTc"
        "wOTE5Mzg3OA@@._V1_SX640_SY720_.jpg",
        ["http://ia.media-imdb.com/images/M/MV5BMTI5MDQzOTY3OV5BMl5BanBnXkFtZT"
         "YwODA1NDc4._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMjk3NTYyMzc4Nl5BMl5BanBnXkFtZT"
         "cwODU3ODMzMw@@._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMTQ0MjU0NzYwMV5BMl5BanBnXkFtZT"
         "YwODk1Mzc3._V1__SX640_SY720_.jpg",
         "http://ia.media-imdb.com/images/M/MV5BMjEyOTkzNjEzMF5BMl5BanBnXkFtZT"
         "YwNjY1Mzc3._V1__SX640_SY720_.jpg"
         ],
        "https://www.youtube.com/watch?v=SUXWAEX2jlg",
        "1999-10-15",
        [" Brad Pitt", "Edward Norton", "Helena Bonham Carter"]
        ))
fresh_tomatoes.open_movies_page(movies)
