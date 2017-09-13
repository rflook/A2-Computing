vals = [7,4,10,3,5,6,12,15]

tree = []
for i in range (0,len(vals)):
    tree.append([vals[i],None, None])

#sort out the links
for i in range(1,len(tree)):
    ptr = 1
    pos = 0
    while ptr != None:
        if tree[i][0] < tree[pos][0]:
            #go left
            ptr = tree[pos][1]
        else:
            #go right
            ptr = tree[pos][2]

        if ptr != None:
            pos = ptr

    if tree[i][0] < tree[pos][0]:
        # go left
        tree[pos][1] = i
    else:
        # go right
        tree[pos][2] = i

print(tree)
