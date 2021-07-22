#Given an array nums, partition it into two (contiguous) subarrays left and right so that:
  #Every element in left is less than or equal to every element in right.
  #left and right are non-empty.
  #left has the smallest possible size.
#Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

#Input: nums = [5,0,3,8,6]
#Output: 3
#Explanation: left = [5,0,3], right = [8,6]

#Input: nums = [1,1,1,0,6,12]
#Output: 4
#Explanation: left = [1,1,1,0], right = [6,12]

#This solution uses two pointers, one the maximum in the left array, and the other the first value in the second array.
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        pointer1 = 0
        pointer2 = -1   #We will not be initializing the second pointer until we find a value which fulfills the second array having larger values.
        
        #We start by defining the largest value in the first array, which will be val1, the maximum value will be used in later in determining where to put the first pointer.
        val1 = nums[pointer1]
        maxVal = val1
        maxIndex = pointer1
        
        #I promised this is O(n) time complexity and this is.
        for i in range(1,len(nums)):
            temp = nums[i]  #trading some memory for more speed in computation.
            
            #We want to keep track of this value because if a value appears in the right array which is smaller than the biggest value in the left array, this value will become
            #the value we want to compare against when choosing where the second array starts since this is the value we ultimately care about.
            if temp > maxVal:
                maxVal = temp
                maxIndex = i
                
            #If the second pointer is uninitialized, we only want to start it where we know at least the first value in the right array is greater than the greatest value 
            #in the left array.
            if temp >= val1 and pointer2 == -1:
                pointer2 = i
                
            #If we run into a value in the right array which is smaller than the largest value in the left array, we need to uninitialize the second pointer because that array
            #no longer fits the goals of the stated problem. We move the maximum value into the first value because this is now the value we are comparing against. We 
            #uninitialize the second pointer because we will now be looking for a value which is greater than the first value, or the maximum in the left array.
            if temp < val1 and pointer2 != -1:
                val1 = maxVal
                pointer1 = maxIndex
                pointer2 = -1
        
        #The problem statement has us returning where the right array begins, and the second pointer fits that bill.
        return pointer2
