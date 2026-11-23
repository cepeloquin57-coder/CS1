#question 1


def countdown(number):
    for i in range(number, -1, -1):
        print(i)
    print("Blastoff!")

def countdown2(number):
    while number > 0:
        print(number)
        number -= 1
    print("Blastoff!")

def countdown3(number):
    if number <0:
        print("Blastoff!")
        return
    print(number)
    countdown3(number-1)

countdown(5)
countdown2(5)
countdown3(5)

#question 2
def rever(string):
    if string == "":
        return string
    else:
        return rever(string[1:])+string[0]
print(rever("hello"))

#question 3
def maze2():
    response = input("You are lost in a maze. Will you go left or right?") #response initialized on first run, updated in recursions
    if response != "left":
        print("You fall in a pit. You lose!") #stop condition
    else:
        maze2()#function calls itself
maze2()

#question 4
#true

#question 5
#false

#question 6
def count_chars(word):
    if word == "":
        return 0
    else:
        return count_chars(word[1:]) + 1
print(count_chars("hello"))

#question 7
def countdown_two(number):
    if number < -1:
        print("Blastoff!")
        return
    print(number)
    countdown_two(number-2)

countdown_two(5)

#question 8
def contains_letter(word,letter):
    if word == "":
        return False
    if word[0] == letter:
        return True
    else:
        if contains_letter(word[1:],letter):
            return True
        else:
            return False
print(contains_letter("hello","h"))
print(contains_letter("hello","q"))

#question 9
def repeat_number(number, n=5):
    if n <= 0:
        print("nul")
    if n == 1:
         print(number)
    else:
        repeat_number(number, n-1)
        print(number)

repeat_number(5)
repeat_number(7)