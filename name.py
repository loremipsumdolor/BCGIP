##########
# Name
# from BASIC Computer Games Microcomputer Edition edited by David H. Ahl
# Game written by Geoffrey Chase of the Abbey, Portsmouth, Rhode Island
# Translated into Python and updated by Jacob Turner
##########

print "Name"
print "by Geoffrey Chase"
print
print "Hello."
print "My name is Creative Computer."
print
name = raw_input("What's your name (first and last)? ").lower()
print "Thank you, %s." % name.title()[::-1]
print "Oops! I guess I got it backwards. A smart"
print "computer like me shouldn't make a mistake like that!"
print
print "But I just noticed that your letters are out of order."
print "Let's put them in order like this: " + ''.join(sorted(name)).strip()
yn = raw_input("Don't you like that better? ").lower()
if yn == "no":
    print "I'm sorry you don't like it that way."
else:
    print "I knew you'd agree!"
print
print "I really enjoyed meeting you %s!" % name.title()
print "Have a nice day!"
