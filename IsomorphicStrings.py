#This uses dynamic programming where the cipher will be stored by an array. If there are more than one letters trying to substitute the program will know there is an
#issue and return false. Then, the program will check the cipher to look for duplicates which would also indicate there is an issue in the solution.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):  #The trivial case where the two strings are unequal.
            return False
        index = 0
        mem = []
        foundLetter = False
        
        #This will populate the array mem looking for whether a letter cipher has been assigned yet. If it has, it will check to see whether the current letter matches
        #if the current letter does not match it returns false, if the letter is not stored, it will store the combination in the array.
        for i in range(len(s)):
            temp = s[i]
            for j in range(len(mem)):
                if temp == mem[j][0] and mem[j][1] != t[i]:
                    return False
                elif temp == mem[j][0]:
                    foundLetter = True
                    break
            if not foundLetter:
                mem.append([temp, t[i]])
                index += 1
            foundLetter = False
            
        #Now, I will check through the stored memory array looking for whether there are multiple letters trying to cipher a single letter, which would indicate
        #the cipher is invalid and falsify the array.
        second = []
        for i in range(len(mem)):
            temp = mem[i][1]
            for j in range(len(second)):
                if temp == second[j]:
                    return False
            second.append(temp)
        
        #If we get to this point we know that the arrays are both fine, so we simply return true.
        return True
