import re

'''
    --- Day 5: Binary Boarding ---
    You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.
    
    You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.
    
    Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".
    
    The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
    
    For example, consider just the first seven characters of FBFBBFFRLR:
    
    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.
    The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.
    
    For example, consider just the last 3 characters of FBFBBFFRLR:
    
    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.
    So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
    
    Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.
'''

def split(input, direction):
    newInput=()
    #newInput1=()
    #for i in range(0,input):
    #    newInput1 = newInput1 + (i ,)

    if direction == "B":
        print("you chose upper")
        temp=()
        for i in range(int(len(input)/2),len(input)):
           temp=temp + (input[i] ,) 
        return(temp)
    elif direction == "F":
        print("you chose lower")
        temp=()
        for i in range(0,int(len(input)/2)):
           if int(len(input)/2) > 1:     
               temp = temp + (input[i] ,)
           else:
               temp = input[i] 

        return(temp)
def makeRows(numberOfRows):
    newInput1=()
    for i in range(0,numberOfRows):
        if numberOfRows > 1:
            print(i)
            print(numberOfRows)
            newInput1 = newInput1 + (i ,)
        else:
            newInput1 = newInput1 + (i)

    return newInput1


file=open("day5-input.sample","r")
#file=open("day5-input","r")
#this re regular expression removes the /n or whatever
temp=file.readlines()

for i in temp:
    print(i.strip("\n"))
number=128
rows=makeRows(128)
print(rows)

split(rows,"B")
remainingrows=split(rows,"B")
print("pritingathing")
print(remainingrows)
remainingrows=split(remainingrows,"B")
print(remainingrows)
remainingrows=split(remainingrows,"B")
print(remainingrows)
remainingrows=split(remainingrows,"F")
print(remainingrows)
remainingrows=split(remainingrows,"B")
print(remainingrows)
remainingrows=split(remainingrows,"F")
print(remainingrows)
remainingrows=split(remainingrows,"F")
print(remainingrows)
