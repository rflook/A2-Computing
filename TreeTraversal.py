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
    steps = 0
    currentPos = 0
    complete = False

    #stack.append(tree[currentPos])

    while complete == False:

        # if we can do neither then print the value and go up one level
        if (tree[currentPos][2] is None) and (tree[currentPos][1] is None):
            outputs.append(tree[currentPos][0])

            # unwind the by going back to the last right branch
            counter = len(stack)-1

            if counter > -1:
                while stack[counter][2] is None:

                    outputs.append(stack[counter][0])
                    currentPos = stack[counter][2]
                    stack.pop()
                    if counter >= 1:
                        counter -= 1
                    else:
                        break

            if len(stack) > 0:
                outputs.append(stack[counter][0])
                currentPos = stack[counter][2]
                stack.pop()

        # check if we can only go right
        elif (tree[currentPos][2] is not None) and (tree[currentPos][1] is None):
            # if can only go right, we need to add to stack change right ptr to none and output the value
            newPos = tree[currentPos][2]
            outputs.append(tree[currentPos][0])
            # stack.append(tree[currentPos])
            tree[currentPos][2] = None
            currentPos = newPos
            # steps += 1

        #check if we can go left
        elif (tree[currentPos][1] is not None):
            newPos = tree[currentPos][1]
            stack.append(tree[currentPos])
            tree[currentPos][1] = None
            currentPos = newPos
            steps += 1

        if len(outputs) == len(tree):
            print(outputs)
            complete = True
