##########
# Acey Ducey
# from the BASIC Computer Games Microcomputer Edition edited by David H. Ahl
# Game written by Bill Palmby of Prairie View, Illinois
# Translated into Python and updated by Jacob Turner
##########

import random

def card_name(number):
    if number == 11:
        return "Jack"
    elif number == 12:
        return "Queen"
    elif number == 13:
        return "King"
    elif number == 14:
        return "Ace"
    else:
        return str(number)

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
    print "Here are your next two cards:"
    print card_name(a) + " and " + card_name(b)
    print
    while True:
        while True:
            bet = raw_input("What is your bet? $")
            if bet.isdigit():
                bet = int(bet)
                break
            else:
                print "Invalid input, please try again."
        if bet > q:
            print "Sorry my friend, but you bet too much."
            print "You only have $" + str(q) + " to bet."
        elif bet == 0:
            print "Chicken!"
            break
        elif bet == "q":
            print "OK. Hope you had fun!"
            break
        else:
            break
    print "The card is a(n) " + card_name(c) + "."
    if a < c < b:
        if bet == 0:
            print "Nothing changes."
        else:
            print "You win!"
            q = q + bet
    else:
        if bet != 0:
            print "Sorry, you lose."
            q = q - bet
        else:
            print "Nothing changes."
        if q == 0:
            again = raw_input("Try again? (yes or no) ")
            if again == "yes":
                q = 100
            elif again == "no":
                print "OK. Hope you had fun!"
                break
        else:
            pass
