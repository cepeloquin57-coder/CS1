
print("====Question 3====")
coffee_per_week = 5 #number of days per week that a person buys a cup of coffee
cost_per_coffee = 2.99 #cost of 1 cup of coffee (I'm guessing honestly, I don't drink coffee)
print(f"The total amount the person spends per week on coffe is ${round(coffee_per_week * cost_per_coffee,2)}")
print("====Question 4====")
name = "caitlin"
name = name.title()
print(f"Hi {name}, How are you?")
print("====Question 5====")
name = "Elizabeth"
print(name.lower())
print(name.upper())
print(name.title())
print("====Question 6====")
print("Terry Pratchett wrote, 'Stories of imagination tend to upset those without one.'")
print("====Question 7====")
famous_person = "Terry Pratchett"
quote = "Stories of imagination tend to upset those without one."
print(f"{famous_person} wrote, '{quote}'")
print("====Question 8====")
name = "        \nPeloquin\t"
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())
print("====Question 9====")
student_quant = 25 #number of students in a class
print(f"The number of groups of three that can be made is {student_quant//3} and there will be {student_quant%3} students left over.")
print("====Question 10====")
temp_f = 70
print(f"The temperature is {temp_f} degrees Fahrenheit. That is about {round((temp_f-32)*(5/9))} degrees Celsius. ")