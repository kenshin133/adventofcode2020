import re
##day 1: 
"""Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

    1721
    979
    366
    299
    675
    1456
    In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

    Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?"""


file=open("day1-input","r")    
#this re regular expression removes the /n or whatever
input=re.findall(r"\S+",file.read())
file.close()
print(input)

for primary in input:
    print("primary is " + str(primary))
    for secondary in input[1:]:
        if primary == secondary:
            #nothing
            continue
        else:
            print("secondary = " + str(secondary))
            added=int(primary) + int(secondary)
            print("added = " + str(added))
            if added == 2020:
                print(str(primary) + " + " + str(secondary) + " = 2020")
                multiplied = int(primary) * int(secondary)
                print("multiplied those it is " + str(multiplied))
                break
