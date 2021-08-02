/*Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1] */

//Using a dynamic programming array, I will be calculating all sums from two values until the closest is found.

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int[,] dp = new int[nums.Length, nums.Length];
        int largest = Int32.MaxValue;
        int[] index = new int[2];
        
        for(int i = 0; i < nums.Length; i++){
            for(int j = i + 1; j < nums.Length; j++){
                dp[i,j] = nums[i] + nums[j];
                if(Math.Abs(dp[i,j] - target) < largest){
                    largest = Math.Abs(dp[i,j] - target);
                    index[0] = i;
                    index[1] = j;
                }
                if(dp[i,j] == target){
                    return(index);
                }
            }
        }
        return(index);
        
    }
}
