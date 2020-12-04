import re
##day 1: 
"""--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?"""


file=open("day1-input","r")    
#this re regular expression removes the /n or whatever
input=re.findall(r"\S+",file.read())
file.close()
print(input)

for primary in input:
    #print("primary is " + str(primary))
    for secondary in input[1:]:
        if primary == secondary:
            #nothing
            continue
        else:
            for tertiary in input[2:]:
                #print("tertiary = " + str(tertiary))
                added=int(primary) + int(secondary) + int(tertiary)
                #print("added = " + str(added))
                if added == 2020:
                    print("we found 2020")
                    multiplied = int(primary) * int(secondary) * int(tertiary)
                    print("multiplied those it is " + str(multiplied))
                    break
