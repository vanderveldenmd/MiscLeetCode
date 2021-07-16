#What I will be doing is iterating through the array using modified brute-force methods in order to find unique solutions for the problem. The array nums are all the integers
#to possibly use and target is the value we are looking for.

#For example: given nums = [1,0,-1,0,-2,2] and target = 0
#The return value should be [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        mem = {}  #I will be using a dictionary in order to ensure we don't have duplicate values for answers since we are looking for unique combinations.
        nums.sort()   #As part of the modified brute-force method I need the array to be in order from smallest to largest, more on that later.
        returnArray = []  #the answer wants it returned in an array, this is that array.
        if len(nums) < 4:   #A trivial answer whereby there aren't enough values to get a real target sum
            return returnArray
        
        #modified brute force means that I will be looking through each of of the first three numbers and trying to find a fourth which matches the target. So I need to keep
        #track of these values and find a fourth.
        pointer1 = 0
        pointer2 = 1
        pointer3 = 2
        
        lenNums = len(nums)   #This is simply to speed up the process a bit.
        
        #pointer1 can't be more than lenNums - 3 because than there aren't enough values for the other pointers in the array, pointer2 can't be more than lenNums - 2 and so on.
        while pointer1 < lenNums - 3:
            while pointer2 < lenNums - 2:
                while pointer3 < lenNums - 1:
                  #This is the final value we will be looking for in the array.
                    newTarget = target - (nums[pointer1] + nums[pointer2] + nums[pointer3])
                    
                    #A trivial solution whereby an answer can't be found within the array as the value we are looking for is either too big or too small to solve.
                    if not newTarget > nums[lenNums - 1] and not newTarget < nums[pointer3 + 1]:
                    
                        #I said this is modified brute-force and this is where that comes into play. This will use a binary search to find the fourth value.
                        left = pointer3 + 1
                        right = lenNums - 1
                        
                        #I slightly modified the binary search to make it account for the value might not be present within the array but it will work all the same.
                        while left <= right:
                            mid = int((left + right) / 2)
                            if newTarget < nums[mid]:
                                if left == right:
                                    left = mid + 2
                                else:
                                    right = mid - 1
                            elif newTarget > nums[mid]:
                                if left == right:
                                    left = mid + 2
                                else:
                                    left = mid + 1
                            else:
                              #When a value is found a new entry will be entered in the dictionary, note that this will overwrite duplicate keys so we only have uniques.
                                mem[(nums[pointer1],nums[pointer2],nums[pointer3],nums[mid])] = 0
                                left = right + 1
                    #When a value is found we continue to iterate through the array by moving the pointers to the right.
                    pointer3 += 1
                pointer2 += 1
                pointer3 = pointer2 + 1
            pointer1 += 1
            pointer2 = pointer1 + 1
            pointer3 = pointer2 + 1

        #The answer wants an array returned so here I am simply coverting the dictionary to an array and returning said array for the solution.
        for i in mem.keys():
            returnArray.append(i)

        return returnArray
