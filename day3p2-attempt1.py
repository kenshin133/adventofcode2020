import re
from array import *
#this is broken, it was never saved after the first challenge and is now half finished part two code. It should still work for the original puzzle Its
#its hard to say
'''--- Day 3: Toboggan Trajectory ---
    With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.
    
    Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle test) of the open squares (.) and trees (#) you can see. For example:
    
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
    These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:
    
    ..##.........##.........##.........##.........##.........##.......  --->
    #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........#.#........#.#........#.#........#.#........#.#........#
    #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
    #...##....##...##....##...##....##...##....##...##....##...##....#
    .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
    You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).
    
    The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:
    
    From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.
    
    The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:
    
    ..##.........##.........##.........##.........##.........##.......  --->
    #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........#.#........X.#........#.#........#.#........#.#........#
    #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
    #...##....##...##....##...#X....##...##....##...##....##...##....#
    .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
    In this example, traversing the map using this slope would cause you to encounter 7 trees.
    
    Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?'''

#is this one we will start with the sample test which results in 7 trees hit, then we will use the real test
def growArray(input, slope):
    for i in range(0,len(input)):
        slope[i]=slope[i]+input[i]

def checkNext(slope, addx, addy):
    global locationy
    if (locationx + addx) <= len(slope[addy]) and locationy + addy <= len(slope)-1:
        #print("posx is " + str(posx))
        #print("slope is " + str(len(slope[1])) + " wide")
        return 0
    elif locationy + addy >= len(slope)-1:
        #print (locationy)
        #print (addy)
        #print (len(slope))
        locationy+1
        return 0


def move(slope,addx,addy):
    global locationy,locationx,trees,bottom
    #print("pos is [" + str(locationx) + "][" + str(locationy) + "]")
#    print("pos is [" + str(locationx) + "][" + str(locationy) + "]")
    #print(locationy)
    #print(len(slope))
    #print(locationx)
    #print(len(slope[1]))
    if locationy == len(slope)-1:
        #print("YOU WIN")
        #print(trees)
        bottom=1
    elif slope[locationy][locationx] == "#":
        trees=trees+1
        #print("TREEEEEEEE oof!")
        locationy = locationy+addy
        locationx = locationx+addx
    else:
        #print("dirt")
        locationy = locationy+addy
        locationx = locationx+addx
def checkSlope(pathx,pathy): 
    print(str(pathx) + " x " + str(pathy))
    global locationx, locationy
    while bottom==0:
        if checkNext(slope,pathx,pathy) == 0:
        #    print(locationy)
            move(slope,pathx,pathy)
        #   print(locationy)
        else:
            growArray(input,slope)
    return trees

file=open("day3-input.sample","r")
#file=open("day3-input","r")
#this re regular expression removes the /n or whatever
input=re.findall(r"\S+",file.read())
file.close()


slope=input.copy()
#we may need to kind of do an 3d array and then maybe a method to grow the array if you reach the edge
#growArray(input,slope)

locationx=0
locationy=0

for i in slope:
    print(i)
bottom = 0
trees = 0
pathx=3
pathy=1
#print("below should be 2 trees)
#slope1=checkSlope(1,1)
#print("hit trees: " + str(trees))
#locationx=0
#locationy=0
#bottom = 0
#trees = 0
#print("below should be 7 trees)
#slope2=checkSlope(3,1)
#print("hit trees: " + str(trees))
#bottom = 0
#trees = 0
#print("below should be 3 trees)
slope3=checkSlope(5,1)
print("hit trees: " + str(trees))
locationx=0
locationy=0
bottom = 0
trees = 0
#print("below should be 4 trees)
slope4=checkSlope(7,1)
#print("hit trees: " + str(trees))
#locationx=0
#locationy=0
#bottom = 0
#trees = 0
#print("below should be 2 trees)
#slope5=checkSlope(1,2)
print("hit trees: " + str(trees))
#print("answer is :" + str(slope5 * slope4 * slope3 * slope2 * slope1))
