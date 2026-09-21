movie_names= ["Titanic", "The Princess Bride", "The Sound of Music", "The Devil Wears Prada", "Casablanca"]
movie_names.append("Singing in the Rain")
movie_names.insert(4,"The Godfather")
movie_names[0] = "The Matrix"
print(movie_names [0])
print(movie_names [-1])
print(len(movie_names))
for movie_name in movie_names:
    print(movie_name)
first_three_movie_names = movie_names [:3]
print(first_three_movie_names)