from pathlib import Path
#Problem 1
name = input("Enter your name: ")
guest_path = Path('guest.txt')
guest_path.write_text(name)

#Problem 2
while True:
    guest_name = input("Enter your name: ")
    book_path = Path('guest_book.txt')
    with book_path.open('a') as f:
        f.write(guest_name)
        f.write("\n")
    if guest_name == "":
        break

#Problem 3
while True:
    reason = input("Enter your reason to like programming: ")
    reason_path = Path('programming_poll.txt')
    with reason_path.open('a') as f:
        f.write(reason)
        f.write("\n")
    if reason == "":
        break

#Problem 4
a = input("Enter a number: ")
b = input("Enter another number: ")
try:
    print(int(a) + int(b))
except ValueError:
    print("Sorry, you have to enter a whole number")

#Problem 5
cat_path = Path('cats.txt')
print('CATS')
try:
    cat_contents = cat_path.read_text()
except FileNotFoundError:
    print("Sorry, I can't find the cat file")
else:
    cat_lines = cat_contents.splitlines()
    for cat_line in cat_lines:
        print(cat_line)
dog_path = Path('dogs.txt')
print('DOGS')
try:
    dog_contents = dog_path.read_text()
except FileNotFoundError:
    print("Sorry, I can't find the dog file")
else:
    dog_lines = dog_contents.splitlines()
    for dog_line in dog_lines:
        print(dog_line)

#Problem 6
rating_path = Path('movie_ratings.txt')
while True:
    rating = input("Enter your rating for the movie(1 to 5): ")
    if rating == "":
        break
    else:
        rating = int(rating)
        if rating > 5 or rating < 1:
            print("Sorry, your rating must be between 1 and 5")
        else:
            with rating_path.open('a') as f:
                f.write(str(rating))
                f.write("\n")
movie_contents = rating_path.read_text()
movie_lines = movie_contents.splitlines()
rating_list = []
for movie in movie_lines:
    rating_list.append(int(movie))
average_path = Path('average_rating.txt')
try:
    average_rating = sum(rating_list) / len(rating_list)
except ZeroDivisionError:
    print("Wow! I can't believe you haven't rated any movies!")
else:
    print(f'Your average rating is {average_rating}')
    average_path.write_text(str(average_rating))

#Problem 7
import json
fav_num_path = Path('fav_num.json')
if fav_num_path.exists():
    num_contents = fav_num_path.read_text()
    fav_num = json.loads(num_contents)
    print(f"I know your favorite number! It's {fav_num}.")
else:
    fav_num = input("Enter your favorite number: ")
    try:
        fav_num = int(fav_num)
    except ValueError:
        print("Sorry, you have to enter a whole number")
    except TypeError:
        print("Sorry, you have to enter a whole number")
    else:
        num_contents = json.dumps(fav_num)
        fav_num_path.write_text(num_contents)
        print(f"Your favorite number is {fav_num}. I'll remember it!")

#Problem 8
fav_food_path = Path('favorite_food.json')
fav_food = input("Enter your favorite food: ")
food_contents = json.dumps(fav_food)
with fav_food_path.open('a') as f:
    f.write(food_contents)
    f.write("\n")
print(f"We'll remember that your favorite food is {fav_food}.")

#Problem 9
student_info = {}
