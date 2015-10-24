##########
# Buzzword
# from BASIC Computer Games Microcomputer Edition edited by David H. Ahl
# Game written by David Ahl
# Translated into Python and updated by Jacob Turner
##########

import random

words = ["ability", "basal", "behavioral", "child-centered", \
         "differentiated", "discovery", "flexible", "heterogeneous", \
         "homogeneous", "manipulative", "modular", "tavistock", \
         "individualized", "learning", "evaluative", "objective", \
         "cognitive", "enrichment", "scheduling", "humanistic", \
         "integrated", "non-graded", "training", "vertical age", \
         "motivational", "creative", "grouping", "modification", \
         "accountability", "process", "core curriculum", "algorithm", \
         "performance", "reinforcement", "open classroom", "resource", \
         "structure", "facility", "environment"]

print "Buzzword Generator"
print "by David H. Ahl"
print
print "This program prints highly acceptable phrases in"
print "'educator-speak' that you can work into reports"
print "and speeches."
print

while True:
    print " ".join(random.sample(words, 3)).capitalize()
    yn = raw_input("Would you like another? ")
    if yn.lower()[0] == "y":
        print
    else:
        break
