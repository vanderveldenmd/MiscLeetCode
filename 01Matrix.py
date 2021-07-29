#Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

#The distance between two adjacent cells is 1.

#Example 1:
#Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
#Output: [[0,0,0],[0,1,0],[0,0,0]]

#Example 2:
#Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
#Output: [[0,0,0],[0,1,0],[1,2,1]]


#This solution will look at each position in the matrix outside to in. So I will be looking for places where a solution is possible working from the smallest numbers to the
#largest. I'll get more on that in a second.
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        newMat = mat
        count = 0
        mem = []
        #We will be storing where we need to look for values in an array, mem as we don't want to have to iterate through the matrix more than we need to.
        
        #This is establishing where we already know we have solutions and where we need to find them. If the matrix is already a zero, we leave it alone. If not, we store
        #that position to be calculated later.
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    count += 1 
                else:
                    newMat[i][j] = -1
                    mem.append([i,j])
        
        #Index will be used to keep track of where we are in the solution. For the first loop, we will be looking for cells whose solution is one cell away from an answer.
        #This will mean that it is in close proximity to a zero. For the second loop, we will be looking for a "1" because these cells are one away from the solution.
        #In this way we will be using previous solutions in order to find the new solutions, making this a dynamic problem. I am solving it this way because this will guarantee
        #that the solution for each cell will be the smallest possible value.
        index = 0
        total = len(mat) * len(mat[0])
        while count < total:
            running = len(mem)
            for i in range(running):
                [row, col] = mem.pop(0) #if we find a solution to this cell, it will remain popped, so it doesn't reappear later.
                if row + 1 < len(mat) and newMat[row + 1][col] == index:
                    newMat[row][col] = index + 1
                    count += 1
                elif col + 1 < len(mat[0]) and newMat[row][col + 1] == index:
                    newMat[row][col] = index + 1
                    count += 1
                elif row - 1 >= 0 and newMat[row - 1][col] == index:
                    newMat[row][col] = index + 1
                    count += 1
                elif col - 1 >= 0 and newMat[row][col - 1] == index:
                    newMat[row][col] = index + 1
                    count += 1
                else:
                    mem.append([row, col])  #if we don't find a solution, we put this cell back into memory to be solved later.
            index += 1
        return newMat
