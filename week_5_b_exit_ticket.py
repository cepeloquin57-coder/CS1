#Question 1
from logging import RootLogger

string = "Aarna"
print(string.title()[1] == "a" and  3 < 5)

#Question 2
musician = "Pyotr Ilyich Tchaikovsky"
if musician == "Freddie Mercury":
    print(f"{musician.title()} is the greatest musician of all time.")
else:
    print(f"{musician.title()} is not the greatest musician of all time.")

#Question 3
#This code produces the absolute value of the variable
variable = -7
if not variable < 0:
    print(variable)
else:
    print(-variable)

#Question 4
professor = "John Pike"
cs_professor = False
if cs_professor == True:
    print(f"Professor {professor.title()} teaches computer science.")
else:
    print(f"Professor {professor.title()} does not teach computer science.")

#Question 5
gpa = 4.0
if gpa == 4.0:
    print("You are eligible for the award.")
#the error in this piece of code was the single equals sign in line 26
#I fixed it by turning it into a Boolean operator

#Question 6
countries_list = ["Brazil", "China", "Cabo Verde", "Haiti", "Portugal", "USA"]
country = "France"
if country in countries_list:
    print(f"A student in this class was born in {country.title()}.")
else:
    print(f"There are no students in this class who were born in {country.title()}.")

#Question 7
age = 21
if age <= 12:
    print("Pay $5.")
if age > 12 and age < 55:
    print("Pay $12.")
if age > 55:
    print("Pay $8.")
#The code is to give prices based on a system that includes discounts for those 12 and under and 55 and older

#Question 8
hours = -1
if hours <= 40 and hours > 0:
    print(f"Wages: ${15*hours}")
elif hours > 40:
    print(f"Wages: ${(15*40)+(1.5*15*(hours-40))}")
elif hours < 0:
    print("ERROR 'negative hours'")

#Question 9
even = []
odd = []
for number in range(1,11):
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(f"Even:{even}")
print(f"0dd: {odd}")

#Question 10
word = "toot"
word = word.lower()
if word[0:] == word[-1::-1]:
    print(f"{word.title()} is a palindrome!")
else:
    print(f"{word.title()} is not a palindrome.")

#Question 11
n = 8
result = 1
if n < 0:
    print("ERROR 'undefined'")
else:
    for i in range(1, n+1):
        result = result * i
print(f"{n}! = {result}")

#Question 12
#Original program was missing closing parenthesis
#corrected program prints each fruit seperately
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print (fruits[i])

#Question 13
#Original program missing colon after if statement
#corrected program prints 6, 8, and 10 each separately
numbers = [2, 6, 8, 3, 10]
for num in numbers:
    if num > 5:
        print(num)
#Question 14
#Program will allow everyone but Mike and David in
#not in [list] does some action for everything but those in that list
#John and Sarah produce true
#John can enter
#Sarah can enter
#Mike cannot enter
#David cannot enter

#Question 15
#35, Fail
#62, B
#78, B
#45, C
#90, A
#runs multiple tests, once it passes one test, executes that code
# if block executed once
# 1st elif executed twice
# 2nd elif executed once
# else block executed once
#35 fails because it is neither >= 80, >=60, nor >=40
#62 gets a B because it is not >= 80, but is >= 60
#78 also gets a B for the same reasons
#45 gets a C because it is nether >=80 nor >=60, but is >=40