#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

#Example 1:

#Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
#Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


#Example 2:
#Input: height = [4,2,0,3,2,5]
#Output: 9

#This solution uses modified two-pointer system whereby I will be checking all values between two local heights in order to find how much water is trapped therein.
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        i = 0
        lastBiggest = 0
        
        #We want to go through the entire array in a linear fashion. This will be done by locating two local peaks and finding the amount of water between the two by adding the
        #rectangles which we can form between the peaks.
        while i < len(height):
          #At the "floor" we don't care because at 0, no water can be trapped. So this will be ignored.
            if height[i] > 0:
              #We will be keeping track of what the current height is because, once we have located two peaks, we will iterate down these peaks until the total water between
              #the two is found.
                curHeight = height[i]
                while curHeight > 0:
                    j = i + 1 #iterator which will be checking right next to the first peak and moving right down the array.
                    #For arrays with much larger values, these variables will be used to speed up the process of calculation. For example, if we have a local array of
                    #[1000,50,5,10001] we only concern ourselves with the values that are actually present, so one iteration is (1000 - 50) * 2 because the length is 2 and
                    #the height of this rectangle is 1000 - 50.
                    lastBiggest = curHeight
                    curBiggest = 0
                    while j < len(height) and height[j] < curHeight:
                        if height[j] > curBiggest:
                          #This will keep track of the next value we can jump to once we have found the highest rectangle in the local peaks.
                            curBiggest = height[j]
                        j += 1
                    if j != len(height):
                      #doing the math on finding the rectangle.
                        water += (lastBiggest - curBiggest) * ((j - i) - 1)
                    curHeight -= (lastBiggest - curBiggest) #Now we set the value for the next local peak and try to form a new rectangle.
                    if lastBiggest == curBiggest:
                        curHeight = 0 #for cases where the area of the rectangle is 0, we know that we have found all water in this location, so we can move on.
                i = j
            else:
                i += 1
        
        return water
