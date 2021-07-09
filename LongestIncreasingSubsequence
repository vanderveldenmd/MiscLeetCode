class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #This array will be storing the number of values BEHIND it in the array which are increasing. So the last value will always be 1 since there is nothing behind itself.
        mem = [0 for i in range(len(nums))]
        current = 0
        smallerMax = 0    #We can use this to evaluate which number behind the given number (if there are more than one that is smaller) will lead to the longer subarray.
        
        #We want to start at the end and work to the front. This will help populate the dp array (mem) and we won't have to calculate the same values more than once, merely
        #check previous values for how many are behind it. This will save time overall.
        for i in range(len(nums)- 1, -1, -1):
            current = nums[i]
            
            #Now we want to check each value behind the current value, trying to find if the value is smaller and, if so, what the longest string that can be made from the new
            #substring that is being formed. Smaller max will help in the case that there are multiple smaller values but some produce longer subarrays than others.
            for j in range(i+1, len(nums)):
                if nums[j] > current:
                    if mem[j] > smallerMax:
                        smallerMax = mem[j]
            mem[i] = 1 + smallerMax   #We use 1 + the smallerMax because the subsequence needs to count the number it is currently looking at.
            smallerMax = 0
        return(max(mem))  #The largest value in this array will be the answer.
