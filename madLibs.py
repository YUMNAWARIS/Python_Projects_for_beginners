"""
User is promt to enter some random words, then program will put those random words in a story. 
Concepts:
- strings
- string concatenation

This can also be done using string formatting and f strings.

"""
person = input("Enter a name: ")
color = input("Enter any color: ")
foods = input("Enter a food name: ")
adjective = input("Enter any adjective: ")
thing = input("Enter noun: ")
place = input("Enter name of a place: ")
verb = input("Enter verb: ")
adverb = input("Enter adverb: ")
food = input("enter food name: ")
things = input("Enter noun: ")

print('Today we picked apple from ' + person + "'s Orchard. I had no idea there were so many different varieties of apples. I ate " + color + ' apples straight off the tree that tested like ' + foods + '. Then there was a ' + adjective + ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple ' + food + ' and ' + things +' pies!.')
