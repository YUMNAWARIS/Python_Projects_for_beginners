"""
This game covers a lot of fundamental topics in python such as:
- random module
- conditions 
- loops
- strings
- lists 
- functions

"""

import random

HANGMAN_PICS = ['''
+---+
    |
    |
    |
   === ''','''
+---+
  O |
    |
    |
   === ''', '''
+---+
  O |
  | |
    |
   === ''', '''
+---+
  O |
 /| |
    |
   === ''', '''
+---+
  O |
 /|\|
    |
   === ''', '''
+---+
  O |
 /|\|
 /  |
   === ''', '''
+---+
  O |
 /|\|
 / \|
   === ''','''
+---+
    |
    |
o-//|
   === '''
]

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def get_random_word(wordlist):
    word_index = random.randint(0, len(wordlist)-1)
    return wordlist[word_index]


def display_board(missed,correct,secret):
    print(HANGMAN_PICS[len(missed_letter)])

    print('MISSED LETTER: ', end=' ')
    if not(missed):
        print("No missed letter")
    for letter in missed:
        print(letter.upper() , end=' ')
    print()

    blank = '-'* len(secret)
    for i in range (len(secret)):
        if secret[i] == correct:
            blank = blank[:i] + secret_word[i] + blank[i+1:]
    for letter in blank:
        print(letter.upper(), end=' ')
    print()


def get_guess(missed_and_correct):
    guess = input("Enter your guess: ")
    while True:
        if len(guess) != 1:
            guess = input("Enter a single character. Try again: ")
        elif guess.lower() in missed_and_correct.lower():
            guess = input("Already gueessed. Try another character: ")
        elif guess.lower() not in 'abcdefghijklmnopqrstuvwxyz':
            guess = input("Invalid input. Enter only letters. Try again: ")
        else:
            return guess

    
missed_letter = ''
correct_letter = ''
game_is_done = False
secret_word = get_random_word(words)


while True:

    display_board(missed_letter,correct_letter,secret_word)

    guess = get_guess(missed_letter+correct_letter)


    if guess in secret_word:
        correct_letter += guess

        foundall = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letter:
                foundall = False
                break
        if foundall:
                print('Yes! The secret word is "' + secret_word.upper() +'"! You have won!')
                game_is_done = True
    else:
        missed_letter += guess
        if len(missed_letter) == len(HANGMAN_PICS)-1:
            display_board(missed_letter,correct_letter,secret_word)
            print('You have run out of guesses!\nAfter ' +str(len(missed_letter)) + ' missed guesses and ' + str(len(correct_letter)) + ' correct guesses, the word was "' + secret_word.upper() + '"')
            game_is_done = True
    
    if game_is_done:
        print('Thank for playing...')
        break
