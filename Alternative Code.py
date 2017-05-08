words = []
for i in range (0,10):
    words.append("(Empty)")

sentence = input("enter your sentence")

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

startWord = -1

for i in range(0,len(sentence)):

    #loop through caps to see if this character is in it
    for j in range(0,len(caps)):
        if sentence[i] == caps[j]:
            startWord = i
            print("caps letter found:" + sentence[i])

            #loop from the current char until we find the next upper case char or we hit the end of the sentence
            endOfWord = False
            nextChar = i+1
            while endOfWord == False and nextChar < len(sentence):

                    #loop through caps to see if this character is in it
                    for k in range(0,len(caps)):
                        if sentence[nextChar] == caps[k]:
                            endOfWord = True

                    nextChar+=1

            if endOfWord==False:
                nextChar+=1

            print(sentence[startWord:nextChar-1])