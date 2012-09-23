'''
Dice
from the BASIC Computer Games Microcomputer Edition edited by David H. Ahl
Game written by Daniel Freidus
Translated into Python by Jacob Turner
'''

import random

print "Dice"
print "by Daniel Freidus"
print
f = [0,0,0,0,0,0,0,0,0,0,0,0]
print "This program simulates the rolling of a pair of dice."
print "You enter the number of times you want the computer to"
print "'roll' the dice. Watch out, very large numbers take"
print "a long time. In particular, numbers over 5000."
print 
x = int(raw_input("How many rolls? "))
for s in range(0,x):
    a = random.randrange(1,7,1)
    b = random.randrange(1,7,1)
    r = a+b-1
    f[r] = f[r]+1
print "Total Spots - Number of Spots"
for v in range(2,13):
    print str(v) + "             " + str(f[v-1])
raw_input("Press Enter to exit.")