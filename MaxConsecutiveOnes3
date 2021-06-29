#Taken from LeetCode daily challenge for 6/29/21
#The goal is to determine the longest sequence of ones that can be made with a certain number of bit flips.
#This program uses the sliding window concept in order to find the largest possible window to get the answer. Since we know that we are allowed a certain number of 0's,
#we only need to find the window that has less than or an equal number of k 0's.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window = len(nums)
        totalZeroes = len(nums) - sum(nums)
        longest = len(nums) - totalZeroes + k   #This will come in handy later.
        if totalZeroes <= k:  #Solving for the trivial solution where the total number is the longest possible.
            return len(nums)
        i = longest
        
        #We set i to be the longest because we know that, even in the base case scenario, that no window can be longer than this because of how many zeroes there are in the
        #entire array versus k.
        while i > 0:
            #localZeroes and leastZeroes will allow us to skip windows, for instance we we try a window size of 10 and always have 2 zeroes, than we know the longest window
            #is AT MOST 8 since that is what this is telling us, so we can skip 9.
            localZeroes = len(nums[0:i]) - sum(nums[0:i])
            leastZeroes = localZeroes
            pointer1 = 0
            pointer2 = i - 1
            while pointer2 < window:  #Here we iterate through different windows using the pointer method.
                if localZeroes <= k:
                    return i
                elif localZeroes < leastZeroes:
                    leastZeroes = localZeroes
                if pointer2 + 1 >= window:
                    break
                #If a 1 is outgoing, than we add to the number of zeros, if there is a one incoming, we subtract from the number of zeroes.
                localZeroes += nums[pointer1]
                localZeroes -= nums[pointer2 + 1]
                pointer1 += 1
                pointer2 += 1
            i -= leastZeroes - k  #As explained above, we can use this to skip windows that can not contain the longest answer.
                
        return 0  #This is for a case where there is an entire array of 0's and k = 0, as this case won't be covered otherwise.
