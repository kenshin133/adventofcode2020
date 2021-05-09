import re

'''
   --- Day 6: Custom Customs ---
    As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.
    
    The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.
    
    However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:
    
    abcx
    abcy
    abcz
    In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)
    
    Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:
    
    This list represents answers from five groups:
    
    The first group contains one person who answered "yes" to 3 questions: a, b, and c.
    The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
    The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
    The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
    The last group contains one person who answered "yes" to only 1 question, b.
    In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.
    
    For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts? 
    --- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
'''

#file=open("day6-input","r")

file=open("day6-input.sample","r")
temp=file.readlines()

#this is from day4 and handles splitting multiple lines into seperate structures based on a blank line
string=""
position=1
passports=[]
sum1=0
for i in temp:
    if i != "\n":
        if string == "":
            string = i.strip('\n')
        else:
            string = string + " " + i.strip('\n')
        if position == len(temp):
            passports.append(string)
            string=""
            position=0
        else:
            position=position+1
        
    else:
        passports.append(string)
        string=""
        position=position+1
print(passports)
for group in passports:
    grouptemp=[]
     
    bigtemp=""
    first=1 
    for d in group:
        if d == " ":
            grouptemp.append(bigtemp)
            bigtemp=""
        else:
            bigtemp=bigtemp+d

    grouptemp.append(bigtemp)
    print(grouptemp)
    #this initiates the first set of letters which can be used to verify the following ones. 
    first=set()
    for i in grouptemp[0]:
        first.add(i)
    for i in grouptemp:
        for f in i:
            if f in first:
                print("this is found in thing" + f)
    set1=set(group)    
    set2=set()    
    for d in group:
        if d == " " or d == "":
            pass
        else:
            if d in set1:
                set2.add(d)
    for i in group.replace(" ",""):
        set1.add(i)
    sum1 = sum1 + len(set1)
    print(sum1)

