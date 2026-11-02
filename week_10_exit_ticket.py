def calculate_average(a,b,c):
    return (a+b+c)/3
def find_highest(a,b,c):
    if a > b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
def find_lowest(a,b,c):
    if a<b:
        if a<c:
            return a
        else:
            return c
    else:
        if b<c:
            return b
        else:
            return c
def check_pass(score):
    if score >= 60:
        return True
    else:
        return False
def display_result(name, average):
    print(f"{name} : {average}")


    menu_running = True
    while menu_running == True:
        print("===Student Grade Management===")
        print("1. Calculate Average")
        print("2. Find Highest Score")
        print("3. Find Lowest Score")
        print("4. Check Pass or Fail")
        print("5. Display Student Result")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            score_1 = float(input("Enter the first score: "))
            score_2 = float(input("Enter the second score: "))
            score_3 = float(input("Enter the last score: "))
            print(f"Average: {round(calculate_average(score_1,score_2,score_3),2)}")
        elif choice == '2':
            score_1 = float(input("Enter the first score: "))
            score_2 = float(input("Enter the second score: "))
            score_3 = float(input("Enter the last score: "))
            print(f"Highest Score: {find_highest(score_1,score_2,score_3)}")
        elif choice == '3':
            score_1 = float(input("Enter the first score: "))
            score_2 = float(input("Enter the second score: "))
            score_3 = float(input("Enter the last score: "))
            print(f"Lowest Score: {find_lowest(score_1,score_2,score_3)}")
        elif choice == '4':
            score_total = float(input("Enter the student average: "))
            if check_pass(score_total) == True:
                print("Pass")
            else:
                print("Fail")
        elif choice == '5':
            student_name = input("Enter the student name: ")
            student_score = input("Enter the student score: ")
            print(f"Average: {round(calculate_average(student_score,student_score,student_name),2)}")
