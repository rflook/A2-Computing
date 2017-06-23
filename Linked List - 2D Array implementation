import random

#this variable is used to keep track of the start node
startNode = -1

names = ["James", "Jemma", "Li Ma", "Shahab", "Nick", "Tim", "Richard", "Pete"]

lList = []
for i in range(0,8):
    lList.append(["",None])

#this variable is so we can point the previous node to the current node
previousLoc = -1

for i in range(0,8):
    #get random name from the names array and drop into the lList
    nameLoc = random.randint(0,len(names)-1)
    name = names[nameLoc]

    print(names)
    print(nameLoc)

    #delete this person from the names list
    names.pop(nameLoc)

    #find a random location to put this in
    isEmpty = None
    while isEmpty != "":
        newLoc = random.randint(0,7)
        isEmpty = lList[newLoc][0]

    #insert the name into this location
    lList[newLoc][0] = name

    #if not the first node, update the pointer of the previous node to this node
    if previousLoc != -1:
        lList[previousLoc][1] = newLoc
    else:
        startNode = newLoc
        
    #sort the pointer
    previousLoc = newLoc

print(lList)
