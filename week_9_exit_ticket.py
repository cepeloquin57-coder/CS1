#Question 1
car = input("What kind of car are you looking for? ")
print(f"Let me see if I can find you a {car}.\n")
#Question 2
party_number =int(input("How many people are in your party for dinner? "))
if party_number > 8:
    print("Sorry, you'll have to wait for a table.\n")
else:
    print("Your table is ready!\n")
#Question 3
picked_num = int(input("Pick a number: "))
if picked_num % 10 == 0:
    print(f"{picked_num} is divisible by 10.\n")
else:
    print(f"{picked_num} is not divisible by 10.\n")
#Question 4
pizza_active = True
while pizza_active == True:
    topping = input("What topping would you like us to add to your pizza?\n Enter 'quit' if you don't want to add any more toppings. ")
    if topping == 'quit':
        pizza_active = False
    else:
        print(f"We'll add {topping} to your pizza.")
print("Thank you for ordering a pizza with us!\n")
#Question 5
while True:
    topping = input("What topping would you like us to add to your pizza?\n Enter 'quit' if you don't want to add any more toppings. ")
    if topping == 'quit':
        break
    else:
        print(f"We'll add {topping} to your pizza.")
print("Thank you for ordering a pizza with us!\n")

topping=""
while topping != "quit":
    topping = input("What topping would you like us to add to your pizza?\n Enter 'quit' if you don't want to add any more toppings. ")
    print(f"We'll add {topping} to your pizza.")
print("Thank you for ordering a pizza with us!\n")
#Question 6
#x=2
#while x>0
    #print(x)
    #x+=1
#Question 7
sandwich_orders = ["BLT", "Chicken Parm", "Italian", "Meatball Sub"]
finished_sandwiches = []
while sandwich_orders != []:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich} sandwich.")
print("I finished all of your sandwiches!\n")
#Question 8
responses = {}
polling = True
while polling == True:
    name = input("What is your name? ")
    response = input("What is your dream vacation? ")
    responses[name] = response
    repeat = input("Would you like to let someone else respond? (yes/no) ")
    if repeat == 'no' or repeat == 'No' or repeat == 'NO':
        polling = False
print("--Dream Vacations--")
for name in responses.keys():
    print(f"{name}: {responses[name]}")
#Question 9
import matplotlib.pyplot as plt
expenses = {}
expenses['Food'] = float(input("How much money do you spend on food each week?"))
expenses['Transportation'] = float(input("How much money do you spend on transportation each week?"))
expenses['Entertainment'] = float(input("How much money do you spend on entertainment each week?"))
plt.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%')
plt.show()
#Question 10
study_hours = {}
study_hours['Python'] = int(input("\nHow many hours did you spend studying Python? "))
study_hours['Math'] = int(input("How many hours did you spend studying math? "))
study_hours['Science'] = int(input("How many hours did you spend studying science? "))
plt.bar(study_hours.keys(), study_hours.values())
plt.xlabel("Subjects")
plt.ylabel("Hours")
plt.title("Study Hours")
plt.show()
#Question 11
print("\n")
temperatures = []
running = True
while running == True:
    temperatures.append(float(input("What is the temperature in degrees F? ")))
    repeat = input('Do you want to enter another temperature (yes/no) ')
    if repeat == 'no' or repeat == 'No' or repeat == 'NO':
        running = False
print(f"All temperatures entered: {temperatures}\nHighest temperature: {max(temperatures)} degrees F\nLowest temperature: {min(temperatures)} degrees F\n")
#Question 12
grades = {}
running = True
while running == True:
    student_name = input("What is the student's name? ")
    student_grade = int(input("What is the student's grade? "))
    grades[student_name] = student_grade
    repeat = input('Do you want to enter another grade (yes/no) ')
    if repeat == 'no' or repeat == 'No' or repeat == 'NO':
        running = False
print(f"--Student Grades--")
for key, value in grades.items():
    print(f"{key}: {value}")
print(f"Average grade: {sum(grades.values())/len(grades.values())}\n")
#Question 13
foods = []
while True:
    foods.append(input("What is one of your favorite foods? "))
    continuing = input("Would you like to add another favorite food? (yes/no) ")
    if continuing == 'no' or continuing == 'No' or continuing == 'NO':
        break
print(foods)
searched_food = input("What food would you like to search for? ")
found = False
for food in foods:
    if food == searched_food:
        found = True
if found == True:
    print(f"{searched_food} is one of your favorite foods.")
else:
    print(f"{searched_food} is not one of your favorite foods.\n")
#Question 14
inventory = {}
while True:
    product_name = input("What is the name of the product you want to add? ")
    product_quant = input(f"How many {product_name}s would you like to add? ")
    inventory[product_name] = product_quant
    repeat = input("Would you like to add another product (yes/no) ? ")
    if repeat == 'no' or repeat == 'No' or repeat == 'NO':
        break
print("--Inventory--")
for key in inventory.keys():
    print(f"{key}: {inventory[key]}")
print(f"Total units: {sum(inventory.values())}\n")
#Question 15
items = []
prices = []
while True:
    items.append(input("What item would you like to purchase? "))
    prices.append(float(input("How much does that cost? ")))
    repeat = input("Would you like to add another item (yes/no) ")
    if repeat == 'no' or repeat == 'No' or repeat == 'NO':
        break
for i in range(len(items)):
    print(f"{items[i]}: {prices[i]}")
    print(f"Total cost: {sum(prices)}")
budget = float(input("What is your budget? "))
if sum(prices) <= budget:
    print(f"You have {budget-sum(prices)} remaining.\n")
else:
    print(f"You are {sum(prices)-budget} over budget.\n")
#Question 16
movies = []
ratings = []
while True:
    movies.append(input("What movie would you like to add? ").title())
    ratings.append(int(input("What would you rate it out of 5? \n(Whole numbers only please!) ")))
    repeat = input("Would you like to add another movie (yes/no) ")
    if repeat == 'no' or repeat == 'No' or repeat == 'NO':
        break
print("--Movies--")
for i in range(len(movies)):
    print(f"{movies[i]}: {ratings[i]}")
print(f"Highest rating: {max(ratings)}\n")
