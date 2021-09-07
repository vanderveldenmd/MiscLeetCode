class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1 == nums2:  #The trivial case where the two are equal
            return len(nums1)
        else:
            maximum = 0 #Storage used to find the longest subarray
            
            #This next section of code initializes the dp array which will contain values of the two given arrays plus enough space to check for subarrays.
            dp = [[0 for i in range(len(nums1) + 1)] for j in range(len(nums2) + 1)]
            for i in range(len(nums1)):
                dp[0][i + 1] = nums1[i]
            for i in range(len(nums2)):
                dp[i + 1][0] = nums2[i]
                
            #In order to populate the subarray we have to check two things. First, if the values of the row and column header are equal, we know that we have a match.
            #We also need to check whether that set is part of an existing subarray. In order to do this, we check the relationship between the diagonally-placed cell.
            #This cell would represent the last number or section of the subarray, if this has a number, we add it to the current cell since we know that is a continuation of
            #an existing array. If it is not, we know that it starts a new subarray. We fill out the entire dp matrix and use it to find the maximum length.
            for i in range(1, len(nums1) + 1):
                for j in range(1, len(nums2) + 1):
                    if dp[0][i] == dp[j][0]:
                        dp[j][i] = 1
                        if i - 1 > 0 and j - 1 > 0:
                            dp[j][i] += dp[j-1][i-1]
                        if dp[j][i] > maximum:
                            maximum = dp[j][i]
        return maximum  #We return maximum to solve the solution.
