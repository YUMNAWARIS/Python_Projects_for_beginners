"""
This is a personal dictionary in which user is prompt to enter a word and then the meaning of that word is displayed on screen.
dictionary.json file is required to run this program which is available on net.
If user enter a word which is not present in a dictionary or a wrong word program will show some closely related words.

"""

import json
from difflib import get_close_matches

words = json.load(open("dictionary"))

def dictionary(search):
    search = search.lower()
    closest_words = get_close_matches(search, words.keys())


    if search in words:
        return(words[search])

    elif len(closest_words)>0:
        print(f"Did you mean {closest_words[0]}? Enter y if yes and n if no...")
        yn = input()
        yn = yn.lower()
        if yn == "y":
            return(words[closest_words[0]])
        elif yn == "n":
            return("The word doesn't exist. Please try a valid word." )
        else:
            return("We didn't understand your entry.")

    else:
        return("The word doesn't exist. Please double check it.")


user_search = input("Enter Word: ")
output = dictionary(user_search)
if type(output) == list:
    for item in output:
        print (item)  

else:
    print(output)

input("Press enter to exist.")