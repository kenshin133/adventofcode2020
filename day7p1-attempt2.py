import re

'''
    --- Day 7: Handy Haversacks ---
    You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

    Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

    For example, consider the following rules:

    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

    You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

    In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
    So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

    How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)
'''



bags = {}
#bags = {'light red bag': ['bright white bag', 'muted yellow bag'],'bright white bag': ['shiny gold bag'],'muted yellow bag': ['shiny gold bags', 'faded blue bags'],'faded blue bags':[],'shiny gold bags':[]}
#'light red bags contain 1 bright white bag, 2 muted yellow bags.\n', 'dark orange bags contain 3 bright white bags,
def splitRule(rule):
    #print(rule)
    rulesplittemp=rule.split(" contain ")
    #print(rulesplittemp)
    rule1=[rulesplittemp[0].replace("bags","bag")]
    rule2=' '.join(rule1)
    #print(f'{rule2} check here')
    #remove number for all numbers also
    templist=[]
    for i in rulesplittemp[1].split(", "):
        if i != 'no other bag':
            templist.append(i.replace("bags","bag").strip(".\n").lstrip('[123456789] '))
    #print(f'{templist} is a temp list and should be the contained bags')
    
    tempDict={rule2:templist}
    #print(tempDict)
    #print(f'bags is {bags}')
    bags.update(tempDict)
    #print(f'{bags} idk should have something else.')
def checkBags(bagColor):
    tempfound=0
    for i in bags[bagColor]:
        if i == 'shiny gold bag':
            tempfound+=1
        elif i == 'no other bag':
            pass
        elif checkBags(i) == 1:
            print("we are going deeper")
            tempfound+=1
        else:
            pass
    if tempfound > 0:
        return 1
    else:
        return 0
potentialBags = 0
#testing structure
#make sure to translate all bags to bag to normalize the data



'''pick a bag
assume it is the "first" bag
check what bags it contains,
    if shiny gold, add 1
    else check other bag colors inside, if shiny gold add 1 and break, or break and move onto next bag
    '''

file=open("day7-input","r")
temp=file.readlines()
print(temp)
#rule="muted yellow bags contain 2 shiny gold bags, 9 faded blue bags."
#print("So you have a shiny gold bag, checking the rules for this")

for rule in temp:
    splitup=splitRule(rule)
    #print(splitup)
for i in bags:
    if checkBags(i) == 1:
        #print(f'{i} can hold a golden bag')
        potentialBags+=1
    else:
        print(f'{i} was not a winner')
    #print(i)
print(potentialBags)


