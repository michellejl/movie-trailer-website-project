import fresh_tomatoes
import media

# Creating a bunch of instances of the class Movie with information
# about several of my favorite movies
harold_and_maude = media.Movie("Harold and Maude",
                               "Young, rich, and obsessed with death, Harold "
                               "finds himself changed forever when he meets "
                               "lively septuagenarian Maude at a funeral.",
                               "1971",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BY2M5Mzg3NjctZTlkNy00MTU0LWFlYTQtY2E2Y2M4NjNiNzllXkEyXkFqcGdeQXVyMTAwMzUyOTc@._V1_.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=0Hh-OEWkC9o"
                               )

apollo_13 = media.Movie("Apollo 13",
                        "NASA must devise a strategy to return Apollo 13 to "
                        "Earth safely after the spacecraft undergoes massive "
                        "internal damage putting the lives of the three "
                        "astronauts on board in jeopardy.",
                        "1995",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNjEzYjJmNzgtNDkwNy00MTQ4LTlmMWMtNzA4YjE2NjI0ZDg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,673,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=nEl0NsYn1fU"
                        )

tommy = media.Movie("Tommy",
                    "A psychosomatically deaf, dumb and blind boy becomes a "
                    "master pinball player and, subsequently, the object of "
                    "a religious cult.",
                    "1975",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjlhZWMyNjItNWU5OS00NGQzLWI4YWYtYThjYjk3OTlmZDA5XkEyXkFqcGdeQXVyMzMyODMwMTI@._V1_SY1000_SX656_AL_.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=G4K_9WyQCgA"
                    )

flash_gordon = media.Movie("Flash Gordon",
                           "A football player and his friends travel to the "
                           "planet Mongo and find themselves fighting the "
                           "tyranny of Ming the Merciless to save Earth.",
                           "1980",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BN2Y4ZDBjMjEtZWQ0OS00NzYyLTg0M2ItMmUzYTEwN2RmMGVlXkEyXkFqcGdeQXVyMjgyOTI1ODY@._V1_SY1000_CR0,0,650,1000_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=PfjZoM_wrV0"
                           )

holy_grail = media.Movie("Monty Python and the Holy Grail",
                         "King Arthur and his knights embark on a low-budget "
                         "search for the Grail, encountering many, very silly "
                         "obstacles.",
                         "1975",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNmNmZjViNTQtNDQ5Mi00MDYzLWI5YWMtNDUyZGNmMGZhNDg4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=LG1PlkURjxE"
                         )

the_wall = media.Movie("The Wall",
                       "A confined but troubled rock star descends into "
                       "madness in the midst of his physical and social "
                       "isolation from everyone.",
                       "1982",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BZDhlZTYxOTYtYTk3Ny00ZDljLTk3ZmItZTcxZWU5YTIyYmFkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,643,1000_AL_.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=PEQEgpyrQ3Q"
                       )

# Create an array of all the movie objects created above to pass
# to fresh_tomatoes
movies = [harold_and_maude, holy_grail, tommy,
          flash_gordon, the_wall, apollo_13]

fresh_tomatoes.open_movies_page(movies)
