#You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

#Count and return the number of maximum integers in the matrix after performing all the operations.

#Example 1:
#Input: m = 3, n = 3, ops = [[2,2],[3,3]]
#Output: 4
#Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.

#Example 2:
#Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
#Output: 4

#Example 3:
#Input: m = 3, n = 3, ops = []
#Output: 9
 
#Constraints:
#1 <= m, n <= 4 * 104
#1 <= ops.length <= 104
#ops[i].length == 2
#1 <= ai <= m
#1 <= bi <= n

#Since we know that the start point and end points are always the same, we can simply get the smallest number in the array, which will be the most accessed cell in either the row
#or the column. Once we know what this is, we can solve.
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
      
        #The trivial solution whereby the entire original array is the largest because none were accessed
        if len(ops) == 0:
            return m*n
        #sort without any parameters will put the smallest of the first two values in the 0'th position so this is the value for mVal or the smallest row
        ops.sort()
        mVal = ops[0][0]
        
        #we find the same value but this time we sort by the second value in order to find the smallest column.
        ops.sort(key = lambda x: x[1])
        nVal = ops[0][1]
        
        #returning the two values multiplied will give the correct answer
        return mVal * nVal
