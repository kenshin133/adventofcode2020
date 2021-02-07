import re




'''
    --- Day 4: Passport Processing ---
    You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.
    
    It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.
    

    Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.
    
    The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:
    
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.
    
    Here is an example batch file containing four passports:
    
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm
    
    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929
    
    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm
    
    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in

    The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).
    
    The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.
    
    The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.
    
    According to the above rules, your improved system would report 2 valid passports.
    
    Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
'''



##TODO normalize file.. perhaps replace newline with --- or something for easier viewing, organizing values, etc.

#file=open("day4-input.sample","r")
file=open("day4-input","r")
#this re regular expression removes the /n or whatever
temp=file.readlines()
#input=re.findall(r"\S+",file.read().split("\n\n"))
#file=open("day3-input.sample","r")
#143 file=open("day3-input","r")
#144 #this re regular expression removes the /n or whatever

#this seemed to work in light testing, if we can just have a loop that terminates whenever a blank space is found and reset. 
string=""
position=1
passports=[]
for i in temp:
    if i != "\n":
        if string == "":
            string = i.strip('\n')
        else:
            string = string + " " + i.strip('\n')
        if position == len(temp):
            print("LAST LINE")
            passports.append(string)
            string=""
            position=0
        else:
            position=position+1
        
    else:
        print("DIE")
        passports.append(string)
        string=""
        position=position+1
#print(passports)
for i in passports:
    print(i)

#data has been normalized at this point and we need to split the info into its specific parts
# the following fields are required besides CID which can be set to optional
#    byr (Birth Year) iyr (Issue Year) eyr (Expiration Year) hgt (Height) hcl (Hair Color) ecl (Eye Color) pid (Passport ID) cid (Country ID)
#format of a passport looks like "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
validPassports=[]
for i in passports:
    invalid=0
    passport={}
    fields=i.split(" ")
    #print(fields)
    for i in fields:
        #i is now the key and value
        key=i.split(':')[0]
        value=i.split(':')[1]
        passport[key]=value
    #print(passport)
    #you can get values using : passport["hcl"]
    #print(passport["hcl"])
    #validate all fields exist
    print(passport)
    requiredFields=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    print(requiredFields)
    for i in requiredFields:
    #    print("checking if " + i + " is in " + str(passport))
        if i in passport:
            print("so far so good")
        else:
            invalid = 1
    if invalid==0:
        validPassports.append(passport)
print(len(validPassports))
