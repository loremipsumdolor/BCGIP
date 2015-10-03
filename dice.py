##########
# Dice
# from BASIC Computer Games Microcomputer Edition edited by David H. Ahl
# Game written by Daniel Freidus, Harrison, New York
# Translated into Python and updated by Jacob Turner
##########

import random

print "Dice"
print "by Daniel Freidus"
print
f = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print "This program simulates the rolling of a pair of dice."
print "You enter the number of times you want the computer to"
print "'roll' the dice. Watch out, very large numbers take"
print "a long time. In particular, numbers over 1000000."
print
while 'x' not in vars():
    x = raw_input("How many rolls? ")
    if x.isdigit():
        x = int(x)
        break
    else:
        print "Invalid number. Please try again."
        del x
for s in range(0, x):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    r = a + b - 1
    f[r] = f[r] + 1
print "Total Spots - Number of Spots"
for v in range(2, 13):
    if len(str(v)) == 1:
        print str(v) + "             " + str(f[v-1])
    else:
        print str(v) + "            " + str(f[v-1])
