#Movie Information
movie_name, movie_genre = "the princess bride", "fantasy"
movie_name = movie_name.title() #ensures proper formatting
movie_genre = movie_genre.title()
movie_release_year, movie_imdb_rating = 1987, 8
MAX_IMDB_RATING = 10
favorite_character, favorite_actor = "Inigo Montoya", "Mandy Patinkin"
favorite_character = favorite_character.title() #unnecessary by my writing, but just in case
favorite_actor = favorite_actor.title()
print(f"====Movie Information====\nMovie: {movie_name}\nGenre: {movie_genre}\nRelease Year: {movie_release_year}\nMovie Rating: {movie_imdb_rating}/{MAX_IMDB_RATING}")