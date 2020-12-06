import re
from array import *
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

def checkNext(slope, posx, locationy):
    if (posx + 3) <= len(slope[1]):
        #print("posx is " + str(posx))
        #print("slope is " + str(len(slope[1])) + " wide")
        return 0


def move(slope,posx,posy):
    global locationy
    print("pos is [" + str(posx) + "][" + str(posy) + "]")
    print("moving one down")
    locationy=locationy+1
    print("pos is [" + str(posx) + "][" + str(posy) + "]")
    if slope[posy][posx] == "#":
        print("TREEEEEEEE")
    else:
        print("dirt")
    
file=open("day3-input.sample","r")
#this re regular expression removes the /n or whatever
input=re.findall(r"\S+",file.read())
file.close()


slope=input.copy()
#we may need to kind of do an 3d array and then maybe a method to grow the array if you reach the edge
#growArray(input,slope)

locationx=0
locationy=8

print("positiing is [" + str(locationx)+"][" + str(locationy) + "]")

bottom = 0
trees = 0
while bottom==0:
    for i in slope:
        print(i)
    if checkNext(slope,locationx,locationy) == 0:
        print(locationy)
        move(slope, locationx,locationy)
        print(locationy)
    else:
        growArray(input,slope)
