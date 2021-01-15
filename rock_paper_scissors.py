"""
Concept Covered:
- random
- conditions
- functions

"""

import random

def play():
    user = input("What's your choice? 'r' for rock, 's' for scissors, 'p' for paper: ")
    computer = random.choice(['r','s','p'])
    print(computer)

    if user == computer:
        return "Tie..."
    
    if if_win(user, computer):
        return "You Won"

    return "you lost!"
    

def if_win(player, opponent):
    if ( player == 'r'and opponent == 'p') or (player == 'p'and opponent == 's') or (player == 's'and opponent == 'r'):
        return True
    

print(play())