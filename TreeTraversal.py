def createTree(vals):
    tree = []
    for i in range (0,len(vals)):
        #value, left pointer, right pointer, parent pointer
        tree.append([vals[i],None, None, None])

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

        tree[i][3] = pos

    return(tree)

#function for in order tree traversal
def inOrder(tree):
    stack = []
    outputs=[]
    startPos = 0
    currentPos = 0
    complete = False
    prevDir = None

    #stack.append(tree[currentPos])

    while complete == False:

        #check if both child links are None
        if (tree[currentPos][2] is None) and (tree[currentPos][1] is None):

            outputs.append(tree[currentPos][0])
            # print and the previous node val make the current node the previous node
            outputs.append(stack[len(stack) - 1][0])
            currentPos = stack[len(stack)-1][2]


            #remove the last item from the stack
            stack.pop()

        #check if we can go left
        print("checking left link")
        if (tree[currentPos][1] is not None):
            stack.append(tree[currentPos])
            print(stack)
            prevDir = "L"
            currentPos = tree[currentPos][1]


        #check if we can only go right
        print("checking right link")
        if (tree[currentPos][2] is not None) and (tree[currentPos][1] is None):
            stack.append(tree[currentPos])
            outputs.append(tree[currentPos][0])
            print(stack)
            currentPos = tree[currentPos][2]
            prevDir = "R"





        #complete = True



    #print(outputs)



#run the code
vals = [7, 4, 10, 3, 5, 6, 12, 15]
tree = createTree(vals)
#print(tree)
inOrder(tree)
