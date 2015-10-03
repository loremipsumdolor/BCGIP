##########
# Change
# from BASIC Computer Games Microcomputer Edition edited by David H. Ahl
# Game written by Dennis Lunder, People's Computer Company
# Translated into Python and updated by Jacob Turner
##########

print "Change"
print "by Dennis Lunder"
print
print "I, your friendly microcomputer, will determine"
print "the proper change for items."
print
a = float(raw_input("Cost of item: "))
p = float(raw_input("Amount of payment: "))
c = p - a
m = c
if c < 0:
    print "You have shortchanged me $" + str(a - p) + "!"
    break
print "Your change: $" + str(c)
d = int(c / 10)
if d > 0:
    print str(d) + " Ten dollar bill(s)"
c = m - (d * 10)
e = int(c / 5)
if e > 0:
    print str(e) + " Five dollar bill(s)"
c = m - (d * 10 + e * 5)
f = int(c)
if f > 0:
    print str(f) + " One dollar bill(s)"
c = (m - (d * 10 + e * 5 + f)) * 100
n = c
g = int(c / 50)
if g > 0:
    print str(g) + " One-half dollar(s)"
c = n - (g * 50)
h = int(c / 25)
if h > 0:
    print str(h) + " Quarter(s)"
c = n - (g * 50 + h * 25)
i = int(c / 10)
if i > 0:
    print str(i) + " Dime(s)"
c = n - (g * 50 + h * 25 + i * 10)
j = int(c / 5)
if j > 0:
    print str(j) + " Nickel(s)"
c = n - (g * 50 + h * 25 + i * 10 + j * 5)
k = int(c + .5)
if k == 1:
    print str(k) + " Penny"
elif k > 2:
    print str(k) + " Pennies"
raw_input("Thank you, come again. Press Enter to exit.")
