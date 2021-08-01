#You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
#Return the size of the largest island in grid after applying this operation.
#An island is a 4-directionally connected group of 1s.

#Example 1:
#Input: grid = [[1,0],[0,1]]
#Output: 3
#Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

#Example 2:
#Input: grid = [[1,1],[1,0]]
#Output: 4
#Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

#Example 3:
#Input: grid = [[1,1],[1,1]]
#Output: 4
#Explanation: Can't change any 0 to 1, only one island with area = 4.


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        #What I will be doing is grouping the islands by giving them all unique numbers and storing these numbers with their areas in a dictionary.
        #This function will do the grouping of the islands and assist by finding their total areas.
        def redefineGrid(x, y, num):
            if grid[x][y] != 1: #if we hit water we can just return zero as there is no need to access this part of the array.
                return 0
            grid[x][y] = num  #Here we will keep track of each mass of 1's by labeling each island.
            area = 1
            if x + 1 < len(grid):
                area += redefineGrid(x + 1, y, num)
            if y + 1 < len(grid[0]):
                area += redefineGrid(x, y + 1, num)
            if x - 1 >= 0:
                area += redefineGrid(x - 1, y, num)
            if y - 1 >= 0:
                area += redefineGrid(x, y - 1, num)
            return area

      
        mem = {}  #mem will be the dictionary.
        current = 2  #Each group of islands gets its own name. We will ignore 1 to make the entire thing easier to begin with.
        subTotal = 0
        totalSize = len(grid) * len(grid[0])
        
        #Now we iterate through the array looking for islands and adding their names and area values to the dictionary.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    subTotal = redefineGrid(i, j, current)
                    if subTotal >= totalSize - 1: #This is a trivial case where either the entire array is 1's or if there is only one 0, in which case, the area is the total
                        return totalSize
                    mem[current] = subTotal
                    current += 1

        #now we will look through the grid once again, this time trying to identify the "water" or 0's and try to use them to connect to different islands.
        #curArray will be used to keep track of which islands are already part of the new landmass so we don't double count islands along the way.
        largest = 0
        curArray = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                  #Setting the stage for the current location by clearing old values.
                    current = 0
                    curArray.clear()
                    if i + 1 < len(grid) and grid[i + 1][j] != 0:
                        current += mem[grid[i + 1][j]]
                        curArray.append(grid[i + 1][j])
                    if i - 1 >= 0 and grid[i - 1][j] != 0 and curArray.count(grid[i - 1][j]) == 0:  #using the array curArray, we keep track of the islands we already counted
                        current += mem[grid[i - 1][j]]
                        curArray.append(grid[i - 1][j])
                    if j + 1 < len(grid[0]) and grid[i][j + 1] != 0 and curArray.count(grid[i][j + 1]) == 0:
                        current += mem[grid[i][j + 1]]
                        curArray.append(grid[i][j + 1])
                    if j - 1 >= 0 and grid[i][j - 1] != 0 and curArray.count(grid[i][j - 1]) == 0:
                        current += mem[grid[i][j - 1]]
                        curArray.append(grid[i][j - 1])
                    #We want to add the current 0 we are looking at, so each current will end up being current + 1
                    if current + 1 > largest:
                        largest = current + 1
        if largest == 0 and totalSize > 0:
        #in another trivial case where the entire array is 0's, we can make a single 1, so we will return 1. Note: the trivial case of a 0-value array is solved below.
            return 1
        return largest
