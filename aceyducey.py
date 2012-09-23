'''
Acey Ducey
from the BASIC Computer Games Microcomputer Edition edited by David H. Ahl
Game written by Bill Palmby
Translated into Python by Jacob Turner
'''

import random, sys

print "Acey Duecy Card Game"
print "by Bill Palmby"
print
print "Acey Ducey is played in the following manner."
print "The dealer (computer) deals two cards face up."
print "You have an option to bet or not bet depending"
print "on whether or not you feel the card will have"
print "a value between the first two."
print "If you do not want to bet, input a 0."
print "Input q to quit at any time."
print
n = 100
q = 100
while True:
    print "You now have $" + str(q) + "."
    print
    while True:
        a = random.randint(2, 14)
        b = random.randint(2, 14)
        c = random.randint(2, 14)
        if a >= b:
            pass
        else:
            break
    while a or b or c == 11 or 12 or 13 or 14:
        if a == 11:
            a = "Jack"
        elif a == 12:
            a = "Queen"
        elif a == 13:
            a = "King"
        elif a == 14:
            a = "Ace"
        elif b == 11:
            b = "Jack"
        elif b == 12:
            b = "Queen"
        elif b == 13:
            b = "King"
        elif b == 14:
            b = "Ace"
        elif c == 11:
            c = "Jack"
        elif c == 12:
            c = "Queen"
        elif c == 13:
            c = "King"
        elif c == 14:
            c = "Ace"
        else:
            break
    print "Here are your next two cards:"
    print str(a) + " and " + str(b)
    print
    while True:
        print "What is your bet?"
        bet = raw_input("> ")
        if bet < q:
            print "Sorry my friend, but you bet too much."
            print "You only have $" + str(q) + " to bet."
        elif bet == 0:
            print "Chicken!"
            break
        elif bet == "q":
            print "OK. Hope you had fun!"
            sys.exit(1)
        else:
            break
    print "The card is a(n) " + str(c) + "."
    while c == "Jack" or "Queen" or "King" or "Ace":
        if c == "Jack":
            c = 11
        elif c == "Queen":
            c = 12
        elif c == "King":
            c = 13
        elif c == "Ace":
            c = 14
        else:
            break
    if c > a and c <= b:
        print "You win!"
        q = q + int(bet)
    else:
        print "Sorry, you lose."
        q = q - int(bet)
        if q == 0:
            while True:
                print "Try again? (yes or no)"
                again = raw_input("> ")
                if again == "yes":
                    q = 100
                elif again == "no":
                    print "OK. Hope you had fun!"
                    sys.exit(1) 
                else:
                    pass