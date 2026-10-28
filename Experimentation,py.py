numbers = [40, 90,66, 70, 45]
max_number = numbers[:]
for i in range(len(numbers)):
    number = numbers[i]
    print(number)
    for item in numbers:
        print(max_number)
        if item < number:
            max_number.remove(item)
print(max_number)