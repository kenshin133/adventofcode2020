import re

'''
    --- Day 7: Handy Haversacks ---
    --- Part Two ---
    It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

    Consider again your shiny gold bag and the rules from the above example:

    faded blue bags contain 0 other bags.
    dotted black bags contain 0 other bags.
    vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
    dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
    So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

    Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

    Here's another example:

    shiny gold bags contain 2 dark red bags.
    dark red bags contain 2 dark orange bags.
    dark orange bags contain 2 dark yellow bags.
    dark yellow bags contain 2 dark green bags.
    dark green bags contain 2 dark blue bags.
    dark blue bags contain 2 dark violet bags.
    dark violet bags contain no other bags.
    In this example, a single shiny gold bag must contain 126 other bags.

    How many individual bags are required inside your single shiny gold bag?
'''



bags = {}
#'light red bags contain 1 bright white bag, 2 muted yellow bags.\n', 'dark orange bags contain 3 bright white bags,
    # new goal is something that looks like : 
    # testingStruct={'light red bag':[{'bright white bag' : 2, 'bright yellow bag':1}]}
def splitRule(rule):

    rulesplittemp=rule.split(" contain ")
    rule1=[rulesplittemp[0].replace("bags","bag")]
    rulekey=' '.join(rule1)
    #print(rulekey)
    templist=[]
    for i in rulesplittemp[1].split(", "):
        #get the number 
        qualtity=0
        #converts the number of bags to a variable.
        numbertmp=filter(str.isdigit, i)
        number= "".join(numbertmp)

        if i != 'no other bag':
            templist.append({i.replace("bags","bag").strip(".\n").lstrip('[123456789] '):str(number)})
        #print(templist)
    #print(f'{templist} is a temp list and should be the contained bags')
    
    tempDict={rulekey:templist}
    #print(f'bags is {bags}')
    bags.update(tempDict)
def countBags(bagColor, number):
    bagsfound=0
    numberofbags=0
    print(f'calculating for {bagColor}')
    #for each color inside the bag rule
    print(f'for i in {bags[bagColor]}')
    for i in bags[bagColor]:
        key = ""
        value = ""
        for k in i.keys():
            key = k
        for v in i.values():
            value = v
        print(f'value : {value} key : {key}')
    #     if i == 'no other bag':
    #         pass
    #     else:
    #         numberofbags=bags[bagColor][0][i]
    #         #print(f'number of bags for {i} is {numberofbags}')
    #         #print(bags[bagColor][0][i])
    #         #print(bags[bagColor])
    #         #print("going deeper")
    #         #add one for the current bag
    #         bagsfound=int(bagsfound) + 1
    #         #add N for the inner bags
    #         bagsfound=bagsfound+countBags(i, numberofbags)
    # print(f'returning {int(bagsfound)*int(number)} total for {bagColor}')
    return int(bagsfound)*int(number)

#testing structure
#make sure to translate all bags to bag to normalize the data



'''Starting with gold bag
    check what is inside shiny gold bag
    resursively check inside each of those and return the total (times the number of bags)
    add up the totals as you go, add, multiply, return
    '''

file=open("day7-input-p2.sample","r")

temp=file.readlines()
#rule="muted yellow bags contain 2 shiny gold bags, 9 faded blue bags."
#print("So you have a shiny gold bag, checking the rules for this")
for rule in temp:
    splitup=splitRule(rule)
    #print(splitup)

bagsNeeded=countBags("dark olive bag", 1)
#print(f'you need {bagsNeeded} to fly')

    #testingStruct={'light red bag':[{'bright white bag' : 2, 'bright yellow bag':1}]}
    #print(testingStruct)
    #This one shows the bags with numbers #{'bright white bag': 2, 'bright yellow bag': 1}
    #print(testingStruct['light red bag'][0])
    #gets a list of keys (or bags) # ['bright white bag', 'bright yellow bag']
    #print(list(testingStruct['light red bag'][0].keys()))
    #starting to use variables # looks like we have 2 number of bright white bag bags
    #                          # looks like we have 1 number of bright yellow bag bags
    #for i in list(testingStruct['light red bag'][0].keys()):
    #    print(f"looks like we have {testingStruct['light red bag'][0][i]} number of {i} bags")
    #this one outputs the number of bags # 2
    #print(testingStruct['light red bag'][0]['bright white bag'])

print(bagsNeeded)
print("the sample answer should be 126")