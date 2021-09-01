/*
You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

The first element in s[k] starts with the selection of the element nums[k] of index = k.
The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
We stop adding right before a duplicate element occurs in s[k].
Return the longest length of a set s[k].

Example 1:
Input: nums = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}

Example 2:
Input: nums = [0,1,2]
Output: 1
 
Constraints:

1 <= nums.length <= 105
0 <= nums[i] < nums.length
All the values of nums are unique.
*/

//Because of the nature of the solution and given the constraints, any array that is valid will be circular, meaning that an array of length 3 will have 1 -> 2, 2->3, and 3->1
//or some combination. We can use this fact in order to solve the problem by changing any visited part of the array to a value which can't otherwise appear so that when we get
//there, we know that that number is already a part of the solution. I'll explain more in the comments.

public class Solution {
    public int ArrayNesting(int[] nums) {
    
        int maxLen = 0;
        int curLen = 0;
        int temp;
        int next;
        
        //This will start with a for loop, going through each of the array values.
        for(int i = 0; i < nums.Length; i++){
            //if a valid number is found (not -1) than we simply go through the array until a loop is closed or a -1 is found in the loop. If a -1 is encountered, we can skip it
            //since it is already included in a different loop.
            if(nums[i] != -1){
                temp = i;
                //the while will run until the entire loop is found, even if that includes the entire array. Changing the value to -1 makes it so that it won't reenter solved loops.
                while(nums[temp] != -1){
                    curLen++;
                    next = nums[temp];
                    nums[temp] = -1;
                    temp = next;
                }
                //if the current loop is longer than the longest loop, we store that in a variable and move on.
                if(curLen > maxLen) maxLen = curLen;
                curLen = 0;
            }
        }
        //We return the longest loop that we have found.
        return(maxLen);
    }
}
