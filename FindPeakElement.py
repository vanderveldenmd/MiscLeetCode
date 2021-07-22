#There are three cases that we care about. If the first value is greater than the second, that is a peak value so we return that index.
#Second case is if there is a peak at the end. If the last value is greater than the second to last value, than that is a peak, so we return that index.
#The third case is if any number is greater than the two that surround it, we know that it is a peak, so we can return that index without any issue.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Solving the trivial case where the list is a single value.
        if len(nums) == 1:
            return 0
        
        #As discussed above, this looks at the various cases and returns the first local value it can find. We may miss other local peaks but since the program problem doesn't
        #care about secondary peaks, neither do I.
        for i in range(len(nums)):
            if i == 0 and nums[i] > nums[i+1]:
                return i
            elif i == len(nums) - 1 and nums[i] > nums[i-1]:
                return i
            else:
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    return i
        #In the case that the list does not contain a local peak, simply return empty since that is what is given in the problem description.
        return
