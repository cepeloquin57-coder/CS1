#Question 1
odd_numbers = list(range(1,20,2))
for odd_number in odd_numbers:
    print(odd_number)
print("------")
#Question 2
mults_of_three = list(range(3,30,3))
for mult_of_three in mults_of_three:
    print(mult_of_three)
print("------")
#Question 3
cubes = []
for num in range(1,11):
    cubes.append(num**3)
for cube in cubes:
    print(cube)
print("------")
#Question 4
#see question 3

#Question 5
scores = [78, 92, 85, 64, 91, 73, 88]
highest_scores = scores[:]
for x in range(len(scores)-2):
    highest_scores.remove(min(highest_scores))
print(highest_scores)
print("------")
#Question 6
numbers_6 = list(range(5,26,5))
numbers_multiplied = []
for index in range(len(numbers_6)):
    numbers_multiplied.append(numbers_6[index]*index)
print(numbers_multiplied)
print("------")
#Question 7
numbers_7 = [7, 1, 5, 3, 6, 4]
numbers_reversed = []
for index in range(len(numbers_7)):
    numbers_reversed.insert(-index, numbers_7[index])
print(numbers_reversed)
print("------")
#Question 8
numbers_8 = [10, 20, 30, 40, 50, 60]
numbers_alternating = []
for index in range(len(numbers_8)//2):
    numbers_alternating.append(numbers_8[index])
    numbers_alternating.append(numbers_8[-index-1])
print(numbers_alternating)
print("------")
#Question 9
numbers_9 = [10, 20, 30, 40, 50, 60, 70, 80]
numbers_even = []
for number_9 in numbers_9:
    print(number_9)
#Question 10
numbers_10 = [10, 20, 30, 40, 50, 60, 70, 80]
numbers_10_copy = numbers_10 [:]
for index in range(2,len(numbers_10),2):


#Question 11