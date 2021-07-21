#Example input and output for such a test case.
#Input: dominoes = ".L.R...LR..L.."
#Output: "LL.RR.LLRRLL.."

#For this solution I will be using flags and a queue in order to determine whether a domino is pushed over or whether it remains standing upright at the end.
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        returnStr = list(dominoes)

        keyArray = []   #The keyArray will be the queue which will hold the dominoes which were pushed last, so these have the potential to push more.

        #This is merely looking through for the first iteration of pushing and popping them into the queue.
        for i in range(len(dominoes)):
            if dominoes[i] == 'L':
                keyArray.append([i,1])
            elif dominoes[i] == 'R':
                keyArray.append([i, 2])

        tempArray = []
        flags = []

      #The while loop will run until there are no more dominoes that can push another.
        while len(keyArray) > 0:
            for i, j in keyArray:
                #keyArray holds the position of the domino which can push and whether it is facing left (1) or right (2)
                if i > 0 and j == 1:
                
                    #This is checking for flags already on the domino. If there is a flag on it or '!' it is already trying to be pushed and therefore can't move.
                    if returnStr[i-1] == '!':
                        returnStr[i-1] = '.'
                    
                    #If the domino is standing upright we flag it for possible pushing in the future.
                    elif returnStr[i-1] == '.':
                        returnStr[i-1] = '!'    #This is putting a flag on the domino
                        flags.append([i - 1, 1])  #We want to check the flag later so we know if it will be pushed over.
                        
                #This if statement does the same as before only with the dominoes which are being pushed right.
                if i < len(dominoes) - 1 and j == 2:
                    if returnStr[i+1] == '!':
                        returnStr[i+1] = '.'
                    elif returnStr[i+1] == '.':
                        returnStr[i+1] = '!'
                        flags.append([i + 1, 2])

            #Now I will be checking whether the flag is still valid by comparing against the returnStr. If it is still '!' we change it.
            for i, j in flags:
                if returnStr[i] == '!':
                    tempArray.append([i, j])  #This is how we will keep track of how many can possibly still change.
                    if j == 1:
                        returnStr[i] = 'L'
                    else:
                        returnStr[i] = 'R'
            flags = []
            tempArray.sort()
            keyArray = tempArray
            tempArray = []

        #When the while loop can't find anything else to change we rejoin the char list and return it as a string, per the challenge guidelines.
        return "".join(returnStr)
