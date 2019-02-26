#!/usr/bin/python3
from favorite_words import begin

## begin ##
print("Please enter two of your favorite words (enter x to quit)")


## testing
while True:
    first_w = input("word one: ")
    if first_w == "x":
        print("Okay, we are closing!")
        break

    sec_w = input("word two: ")
    if sec_w == "x":
        print("Okay, we are closing!")
        break

    fav_string = begin(first_w, sec_w)
    print("Your new favorite stirng is: %s" %(fav_string))
