import re
'''Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?'''

def min(pmin,letter,password):
    print("min is " + str(pmin))
    print(letter)
    print(password)
    print(password.count(letter))
    if int(pmin) <= int(password.count(letter)):
        print("pmin is less than the number")
        return 0
    else:
        print("pmin is higher than number")
        return 1

#return 0 if its below the max
def max(pmax, letter, password):
        print("max is " + str(pmax))
        print(letter)
        print(password)
        print("actual count is")
        print(password.count(letter))
        if int(pmax) >= int(password.count(letter)):
            print("pmax is greater than the number")
            return 0
        else:
            print("pmax is higher than number")
            return 1
def poscheck(pos,letter,password):
    #check if letter is in pos of password
    #print(password[int(pos)-1])
    if password[int(pos)-1] == letter:
        return 0
    else:
        return 1
    

def validate(pmin, pmax, letter, password):
    #print(pmin)
    #print(pmax)
    #print(letter)
    #print(password)

    #if min(pmin, letter, password) == 1:
    #if it is above the min and not above the max
    #if min(pmin, letter, password) == 0 and max(pmax, letter, password) == 0:
    if poscheck(pmin, letter, password) == 0 and poscheck(pmax, letter, password) == 1 or poscheck(pmin, letter, password) == 1 and poscheck(pmax, letter, password) == 0:
        return 0
        
file=open("day2-input","r")
#this re regular expression removes the /n or whatever
input=file.readlines()
file.close()
#print(input)
validPass=0
for i in input:
    split1=re.findall(r"\S+",i)
    policy=split1[0]
    #print (policy)
    split2=policy.split('-')
    #print(split2)
    policyMin=split2[0]
    #print(policyMin)
    policyMax=split2[1]
    #print(policyMax)
    #policyMax=
    #policyMax=
    letter=split1[1].strip(':')
    #print (letter)
    password=split1[2]
    #print (password)
    #print (i)
    if validate(policyMin, policyMax, letter, password) == 0:
        validPass=validPass+1
        print(str(validPass) + " passwords are valid")
    else:
        continue

