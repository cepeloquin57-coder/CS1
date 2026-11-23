movie_names= ["Titanic", "The Princess Bride", "The Sound of Music", "The Devil Wears Prada", "Casablanca"]
movie_names.append("Singing in the Rain")
movie_names.insert(4,"The Godfather")
movie_names[0] = "The Matrix"
print(movie_names [0])
print(movie_names [-1])
print(len(movie_names))
def print_movies(n):
    if n == 1:
        print(movie_names[0])
    else:
        print_movies(n-1)
        print(movie_names[n-1])
print_movies(len(movie_names))
print(movie_names)