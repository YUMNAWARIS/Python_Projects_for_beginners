import random

# for setting max and min (highest and lowest value) of dice
try:
    min_value = int(input("Enter lower limit of dice: "))
    max_value = int(input("Enter upper limit of dice: "))
except:
    print("Invalid Input. Program is revert to default values.")
    min_value = 1
    max_value = 6


try:
    while True:

        # randomize numbers in given range
        print(random.randint(min_value, max_value))

        # ask user for another roll
        another_roll = input("Do you want to roll the dice again? press y to continue! ")
        if another_roll.lower() == 'y':
            continue
        else:
            break
        
    print("Thanks for playing.")

except:
    print("something Went wrong.")
