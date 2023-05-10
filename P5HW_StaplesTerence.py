# This code allows the user to generate a basic math quiz including addition and subtraction.
#04/21/2023
#CTI-110 P5HW - Math Quiz
#Terence Staples

import random

# function for addition
def Addition():
    # getting random integers in range 1 to 100
    a = random.randint(1,100)
    b = random.randint(1,100)
    print("   ",a)
    print(" + ",b)
    # calculating sum
    sum = a+b
    # asking for user's answer
    answer = int(input("\nEnter answer: "))
    # variable to count guesses
    guess = 1
    # loop for getting answer while answer is not correct
    while sum!=answer:
        # if the answer is less than sum print, it is too low
        if answer<sum:
            print("Sorry, guess is too low.")
        # if the answer is more than sum print, it is too high
        else:
            print("Sorry, guess is too high.")
        # again, getting user's input
        answer = int(input("\nTry again: "))
        # incrementing the number of guesses
        guess+=1
    # printing congratulations if the answer is correct
    print("Congratulations!!!! your answer is correct!")
    # printing number of guesses
    print("Number of guesses: ",guess)

# function for subtraction
def Subtraction():
    # getting random integers in range 1 to 100
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print("   ", a)
    print(" - ", b)
    # calculating the difference
    diff = a - b
    # asking for the user's answer
    answer = int(input("\nEnter answer: "))
    # variable to count guesses
    guess = 1
    # loop for getting the answer while answer is not correct
    while diff != answer:
        # if the answer is less than diff print, it is too low
        if answer < diff:
            print("Sorry, guess is too low.")
        # if the answer is more than diff print, it is too high
        else:
            print("Sorry, guess is too high.")
        # again getting user input
        answer = int(input("\nTry again: "))
        # incrementing the number of guesses
        guess += 1
    # printing congratulations if the answer is correct
    print("Congratulations!!!! your answer is correct!")
    # printing number of guesses
    print("Number of guesses: ", guess)

# function to display menu and get user choice
def main():
    # displaying menu
    print("\nMAIN MENU")
    print("-"*20)
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit\n")
    # getting user's input
    option = int(input("Please choose one of the menu options: "))
    # if the option equals to 1 call Addition() function
    if option==1:
        Addition()
    # if the option equals to 2 call Subtraction() function
    elif option==2:
        Subtraction()
    # if the option equals to 3 exit the program
    elif option == 3:
        print("Thank you for playing..")
        print("Bye!!")
        exit()
    # else print invalid option
    else:
        print("Invalid option. Please choose again")
    # again, calling the function until the user exits the program
    main()


print("Welcome to the Math Quiz\n")
main()
