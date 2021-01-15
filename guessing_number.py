"""
Computer selects random number between 1 to 10. User is prompted to guess the number in three trials.

Concepts Covered:
- random
- conditions
- loops
- exception handling

"""

import random

try:
    number = random.randint(1, 10)
    guess = int(input("Guess the number (between 1 to 10). \n"))
    trial = 0

    while trial <= 2:
        if guess < number and trial<=2 :
            print("Guess is too low.")
            guess = int(input("Try again: "))
        elif guess > number and trial<=2:
            print("Guess is too high.")
            guess = int(input("Try again: "))
        elif guess == number and trial<=2:
            print("Your guess is correct. Congratulations! You Win.")
            break
        trial += 1
        
    if guess == number and trial == 3:
        print("Your guess is correct. Congratulations! You Win.")
    else:
        print(f'The number is {number}')
        print("Better lucl next time.")
except:
    print("Something Went wrong. Make sure you enter correct input. ")
